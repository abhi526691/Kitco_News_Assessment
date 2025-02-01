import { useState, useEffect } from "react";
import { useArticles } from "../../context/ArticleContext";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { ArticleFormData } from "../../types/article";
import styles from "./ArticleForm.module.css";

// Updated schema with datetime validation
const articleSchema = z.object({
  title: z.string().min(5, "Title must be at least 5 characters"),
  content: z.string().min(100, "Content must be at least 100 characters"),
  author: z.string().min(3, "Author must be at least 3 characters"),
  publishDate: z.coerce.date({
    required_error: "Please select a date and time",
    invalid_type_error: "That's not a valid date!",
  }),
  status: z.enum(["draft", "published"]),
  category: z.enum(["mining", "crypto"]),
});

interface ArticleFormProps {
  onClose: () => void;
  onSuccess: () => void;
  initialData?: ArticleFormData;
}

const ArticleForm = ({ onClose, onSuccess, initialData }: ArticleFormProps) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<ArticleFormData>({
    resolver: zodResolver(articleSchema),
    defaultValues: initialData,
  });

  const { createArticle, updateArticle } = useArticles();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (initialData) reset(initialData);
  }, [initialData, reset]);

  const onSubmit = async (data: ArticleFormData) => {
    setLoading(true);
    try {
      // Convert to ISO string before submission
      const submissionData = {
        ...data,
        publishDate: new Date(data.publishDate),
      };

      if (initialData) {
        await updateArticle(initialData.id!, submissionData);
      } else {
        await createArticle(data);
      }
      onSuccess();
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.modalBackdrop}>
      <div className={styles.modal}>
        <h2>{initialData ? "Edit Article" : "Create New Article"}</h2>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className={styles.formGroup}>
            <label>Title</label>
            <input {...register("title")} />
            {errors.title && (
              <span className={styles.error}>{errors.title.message}</span>
            )}
          </div>

          <div className={styles.formGroup}>
            <label>Content</label>
            <textarea {...register("content")} rows={6} />
            {errors.content && (
              <span className={styles.error}>{errors.content.message}</span>
            )}
          </div>

          <div className={styles.formRow}>
            <div className={styles.formGroup}>
              <label>Author</label>
              <input {...register("author")} />
              {errors.author && (
                <span className={styles.error}>{errors.author.message}</span>
              )}
            </div>

            <div className={styles.formGroup}>
              <label>Publish Date</label>
              <input type="datetime-local" {...register("publishDate")} />
              {errors.publishDate && (
                <span className={styles.error}>
                  {errors.publishDate.message}
                </span>
              )}
            </div>
          </div>

          <div className={styles.formRow}>
            <div className={styles.formGroup}>
              <label>Status</label>
              <select {...register("status")}>
                <option value="draft">Draft</option>
                <option value="published">Published</option>
              </select>
            </div>

            <div className={styles.formGroup}>
              <label>Category</label>
              <select {...register("category")}>
                <option value="mining">Mining</option>
                <option value="crypto">Crypto</option>
              </select>
            </div>
          </div>

          <div className={styles.buttonGroup}>
            <button type="button" onClick={onClose} disabled={loading}>
              Cancel
            </button>
            <button type="submit" disabled={loading}>
              {loading ? "Saving..." : "Save Article"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ArticleForm;
