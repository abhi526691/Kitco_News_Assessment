import {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
  useCallback,
} from "react";
import { apiClient, ENDPOINTS } from "../api/client";
import { Article, ArticleFormData } from "../types/article";
import toast from "react-hot-toast";

interface ArticleContextType {
  articles: Article[];
  loading: boolean;
  error: string | null;
  searchQuery: string;
  setSearchQuery: (query: string) => void;
  fetchArticles: () => Promise<void>;
  createArticle: (article: ArticleFormData) => Promise<void>;
  updateArticle: (
    id: string,
    article: Partial<ArticleFormData>
  ) => Promise<void>;
  deleteArticle: (id: string) => Promise<void>;
}

const ArticleContext = createContext<ArticleContextType | undefined>(undefined);

export const ArticleProvider = ({ children }: { children: ReactNode }) => {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState("");

  const fetchArticles = useCallback(async () => {
    setLoading(true);
    try {
      const response = await apiClient.get(ENDPOINTS.ARTICLES);
      setArticles(response.data);
    } catch (err) {
      setError("Failed to fetch articles");
      toast.error("Failed to load articles");
    } finally {
      setLoading(false);
    }
  }, []);

  const createArticle = async (article: ArticleFormData) => {
    try {
      const response = await apiClient.post(ENDPOINTS.ARTICLES, article);
      setArticles((prev) => [...prev, response.data]);
      toast.success("Article created successfully");
    } catch (err) {
      toast.error("Failed to create article");
      throw err;
    }
  };

  const updateArticle = async (
    id: string,
    article: Partial<ArticleFormData>
  ) => {
    try {
      const response = await apiClient.put(ENDPOINTS.ARTICLE(id), article);
      setArticles((prev) =>
        prev.map((a) => (a.id === id ? { ...a, ...response.data } : a))
      );
      toast.success("Article updated successfully");
    } catch (err) {
      toast.error("Failed to update article");
      throw err;
    }
  };

  const deleteArticle = async (id: string) => {
    try {
      await apiClient.delete(ENDPOINTS.ARTICLE(id));
      setArticles((prev) => prev.filter((a) => a.id !== id));
      toast.success("Article deleted successfully");
    } catch (err) {
      toast.error("Failed to delete article");
      throw err;
    }
  };

  useEffect(() => {
    fetchArticles();
  }, [fetchArticles]);

  return (
    <ArticleContext.Provider
      value={{
        articles,
        loading,
        error,
        searchQuery,
        setSearchQuery,
        fetchArticles,
        createArticle,
        updateArticle,
        deleteArticle,
      }}
    >
      {children}
    </ArticleContext.Provider>
  );
};

export const useArticles = () => {
  const context = useContext(ArticleContext);
  if (!context)
    throw new Error("useArticles must be used within ArticleProvider");
  return context;
};
