import axios from 'axios';

// export const API_BASE_URL = 'http://localhost:8000';
// const API_BASE_URL = process.env.REACT_APP_API_URL;
// console.log("API URL:", API_BASE_URL);
const API_BASE_URL = import.meta.env.VITE_API_URL;
console.log("API URL:", API_BASE_URL);


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