export interface Article {
  id: string;
  title: string;
  content: string;
  author: string;
  publishDate: Date;
  status: 'draft' | 'published';
  category: 'mining' | 'crypto';
  createdAt: Date;
  updatedAt: Date;
}

export type ArticleFormData = Omit<Article, 'createdAt' | 'updatedAt'>;