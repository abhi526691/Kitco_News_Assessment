import { Article } from "../../types/article";
import styles from "./ArticleDetailModal.module.css";

interface ArticleDetailModalProps {
  article: Article;
  onClose: () => void;
}

const ArticleDetailModal = ({ article, onClose }: ArticleDetailModalProps) => {
  return (
    <div className={styles.modalBackdrop} onClick={onClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <button className={styles.closeButton} onClick={onClose}>
          &times;
        </button>
        <h1 className={styles.title}>{article.title}</h1>
        <div className={styles.meta}>
          <span>By {article.author}</span>
          <span className={styles.status}>{article.category}</span>
          <span>
            Published: {new Date(article.publishDate).toLocaleDateString()}
          </span>
        </div>
        <div className={styles.content}>
          <p>{article.content}</p>
        </div>
      </div>
    </div>
  );
};

export default ArticleDetailModal;
