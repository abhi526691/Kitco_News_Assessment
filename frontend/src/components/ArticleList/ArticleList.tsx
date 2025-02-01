import { useState } from "react";
import { useArticles } from "../../context/ArticleContext";
import ArticleForm from "../ArticleForm/ArticleForm";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner";
import SearchBar from "../SearchBar/SearchBar";
import ArticleDetailModal from "../ArticleDetailModal/ArticleDetailModal";
import styles from "./ArticleList.module.css";
import { useNavigate } from "react-router-dom";
import { Article } from "../../types/article";

const ITEMS_PER_PAGE = 6; // Number of articles to display per page

const ArticleList = () => {
  const {
    articles,
    loading,
    error,
    searchQuery,
    setSearchQuery,
    deleteArticle,
  } = useArticles();
  const navigate = useNavigate();
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [hoveredArticleId, setHoveredArticleId] = useState<string | null>(null);
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [currentPage, setCurrentPage] = useState(1); // Pagination state

  // Filter articles based on search query
  const filteredArticles = articles.filter((article) =>
    article.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Pagination logic
  const totalArticles = filteredArticles.length;
  const totalPages = Math.ceil(totalArticles / ITEMS_PER_PAGE);
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const paginatedArticles = filteredArticles.slice(
    startIndex,
    startIndex + ITEMS_PER_PAGE
  );

  // Handle page change
  const handlePageChange = (page: number) => {
    setCurrentPage(page);
  };

  if (loading) return <LoadingSpinner />;
  if (error) return <div className={styles.error}>{error}</div>;

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Article Dashboard</h1>
        <button
          className={styles.createButton}
          onClick={() => setShowCreateForm(true)}
        >
          Create New
        </button>
      </div>

      <SearchBar value={searchQuery} onChange={setSearchQuery} />

      {showCreateForm && (
        <ArticleForm
          onClose={() => setShowCreateForm(false)}
          onSuccess={() => setShowCreateForm(false)}
        />
      )}

      {selectedArticle && (
        <ArticleDetailModal
          article={selectedArticle}
          onClose={() => setSelectedArticle(null)}
        />
      )}

      <div className={styles.list}>
        {paginatedArticles.map((article) => (
          <div
            key={article.id}
            className={styles.card}
            onMouseEnter={() => setHoveredArticleId(article.id)}
            onMouseLeave={() => setHoveredArticleId(null)}
          >
            <h3>{article.title}</h3>
            <div className="flex justify-between items-center">
              {/* <span>{new Date(article.createdAt).toLocaleDateString()}</span> */}
              <span
                className={`${styles.status} ${
                  article.status === "draft" ? styles.draft : styles.published
                } ml-2`}
              >
                {article.status}
              </span>
            </div>

            {hoveredArticleId === article.id && (
              <div className={styles.contentPreview}>
                <p>{article.content.slice(0, 150)}...</p>
              </div>
            )}

            <div className={styles.actions}>
              <button
                className={styles.viewButton}
                onClick={() => setSelectedArticle(article)}
              >
                View
              </button>
              <button
                className={styles.editButton}
                onClick={() => navigate(`/articles/${article.id}/edit`)}
              >
                Edit
              </button>
              <button
                className={styles.deleteButton}
                onClick={() => {
                  if (
                    window.confirm(
                      "Are you sure you want to delete this article?"
                    )
                  ) {
                    deleteArticle(article.id);
                  }
                }}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Pagination Controls */}
      <div className={styles.pagination}>
        <button
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
          className={styles.paginationButton}
        >
          Previous
        </button>
        <span className={styles.pageIndicator}>
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
          className={styles.paginationButton}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default ArticleList;
