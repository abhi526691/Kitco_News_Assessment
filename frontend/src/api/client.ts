import axios from 'axios';

export const API_BASE_URL = 'http://localhost:8000';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchArticles = async (skip: number, limit: number) => {
  const response = await apiClient.get('/articles', {
    params: { skip, limit },
  });
  return response.data;
};

export const ENDPOINTS = {
  ARTICLES: '/articles',
  ARTICLE: (id: string) => `/articles/${id}`,
};