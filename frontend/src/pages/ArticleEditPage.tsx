import { useParams } from "react-router-dom";
import { useArticles } from "../context/ArticleContext";
import ArticleForm from "../components/ArticleForm/ArticleForm";
import { useEffect, useState } from "react";
import { Article } from "../types/article";

const ArticleEditPage = () => {
  const { id } = useParams();
  const { articles } = useArticles();
  const [article, setArticle] = useState<Article | null>(null);

  useEffect(() => {
    const foundArticle = articles.find((a) => a.id === id);
    if (foundArticle) setArticle(foundArticle);
  }, [id, articles]);

  if (!article) return <div>Loading...</div>;

  return (
    <div>
      <ArticleForm
        initialData={article}
        onClose={() => window.history.back()}
        onSuccess={() => window.history.back()}
      />
    </div>
  );
};

export default ArticleEditPage;
