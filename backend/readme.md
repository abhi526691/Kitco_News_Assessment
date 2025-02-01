# Article Management API

This is a RESTful API for managing articles, built with **FastAPI** and **MongoDB**. It provides endpoints for creating, reading, updating, and deleting articles, along with proper validation and error handling.

---

## Table of Contents

1. [Features](#features)
2. [Technologies](#technologies)
3. [Setup](#setup)
4. [API Endpoints](#api-endpoints)
5. [Request/Response Examples](#requestresponse-examples)
6. [Error Handling](#error-handling)
7. [Environment Variables](#environment-variables)
8. [Testing](#testing)
9. [License](#license)

---

## Features

- **CRUD Operations**: Create, read, update, and delete articles.
- **Validation**: Input validation using Pydantic and Joi.
- **Pagination**: List articles with pagination support.
- **Search**: Basic search functionality.
- **Error Handling**: Proper HTTP status codes and error messages.
- **Logging**: Request/response logging for debugging.
- **Security**: Basic security headers and CORS configuration.

---

## Technologies

- **Python**: Programming language.
- **FastAPI**: Web framework for building APIs.
- **MongoDB**: NoSQL database for storing articles.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server for running FastAPI.
- **Joi**: Input validation for request payloads.

---

## Setup

### Prerequisites

- Python 3.8+
- MongoDB (local or cloud)
- Pipenv (optional, for virtual environment management)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/article-management-api.git
   cd article-management-api
   ```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:<br>
   Create a .env file in the root directory:
   ```bash
   MONGODB_URL=mongodb+srv://username:password.qdpo3.mongodb.net/db_name?retryWrites=true&w=majority&appName=speer
   ```
4. Run the application:
   
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API:
- Local: http://localhost:8000
- Docs: http://localhost:8000/docs (Swagger UI)

# API Endpoints

## Base URL
http://localhost:8000


## Endpoints

| Method  | Endpoint                  | Description                     |
|---------|---------------------------|---------------------------------|
| **GET**  | `/articles`               | List all articles (with pagination) |
| **POST** | `/articles`               | Create a new article           |
| **GET**  | `/articles/{article_id}`  | Get a single article by ID     |
| **PUT**  | `/articles/{article_id}`  | Update an article by ID        |
| **DELETE** | `/articles/{article_id}` | Delete an article by ID        |


### Request/Response Examples

1. List Articles (GET /articles)
   #### Request
   ```bash
   GET /articles?skip=0&limit=10
   ```
   #### Response
   ```bash
      [
     {
       "id": "507f1f77bcf86cd799439011",
       "title": "Blockchain Trends 2023",
       "content": "Detailed analysis of current blockchain trends...",
       "author": "John Doe",
       "publishDate": "2023-10-01T00:00:00",
       "status": "published",
       "category": "crypto",
       "createdAt": "2023-10-01T12:00:00",
       "updatedAt": "2023-10-01T12:00:00"
     }
   ]
   ```

   2. Create Article (POST /articles)
   #### Request
   ```bash
   POST /articles
   Content-Type: application/json
   
   {
     "title": "New Article",
     "content": "This is a new article.",
     "author": "Jane Doe",
     "publishDate": "2023-10-15T00:00:00",
     "status": "draft",
     "category": "mining"
   }
   ```
   #### Response
   ```bash
   {
     "id": "507f1f77bcf86cd799439012",
     "title": "New Article",
     "content": "This is a new article.",
     "author": "Jane Doe",
     "publishDate": "2023-10-15T00:00:00",
     "status": "draft",
     "category": "mining",
     "createdAt": "2023-10-15T12:00:00",
     "updatedAt": "2023-10-15T12:00:00"
   }
   ```

   3. Get Article (GET /articles/{article_id})
   #### Request
   ```bash
   GET /articles/507f1f77bcf86cd799439011
   ```
   #### Response
   ```bash
   {
     "id": "507f1f77bcf86cd799439011",
     "title": "Blockchain Trends 2023",
     "content": "Detailed analysis of current blockchain trends...",
     "author": "John Doe",
     "publishDate": "2023-10-01T00:00:00",
     "status": "published",
     "category": "crypto",
     "createdAt": "2023-10-01T12:00:00",
     "updatedAt": "2023-10-01T12:00:00"
   }
   ```

   4.Update Article (PUT /articles/{article_id})
   #### Request
   ```bash
   PUT /articles/507f1f77bcf86cd799439011
   Content-Type: application/json
   
   {
     "title": "Updated Blockchain Trends 2023",
     "status": "published"
   }
   ```
   #### Response
   ```bash
   {
     "id": "507f1f77bcf86cd799439011",
     "title": "Updated Blockchain Trends 2023",
     "content": "Detailed analysis of current blockchain trends...",
     "author": "John Doe",
     "publishDate": "2023-10-01T00:00:00",
     "status": "published",
     "category": "crypto",
     "createdAt": "2023-10-01T12:00:00",
     "updatedAt": "2023-10-15T12:00:00"
   }
   ```

   4.Delete Article (DELETE /articles/{article_id})
   #### Request
   ```bash
   PUT /articles/507f1f77bcf86cd799439011
   Content-Type: application/json
   
   {
     "title": "Updated Blockchain Trends 2023",
     "status": "published"
   }
   ```
   #### Response
   ```bash
   {
     "id": "507f1f77bcf86cd799439011",
     "title": "Updated Blockchain Trends 2023",
     "content": "Detailed analysis of current blockchain trends...",
     "author": "John Doe",
     "publishDate": "2023-10-01T00:00:00",
     "status": "published",
     "category": "crypto",
     "createdAt": "2023-10-01T12:00:00",
     "updatedAt": "2023-10-15T12:00:00"
   }
   ```


   ## Error Handling

   The API returns appropriate HTTP status codes and error messages:
   
   | Status Code | Description                      |
   |------------|----------------------------------|
   | **400**    | Bad Request (Invalid input)     |
   | **404**    | Not Found (Article not found)   |
   | **500**    | Internal Server Error           |

   ## Example Error Response:
   ```bash
   {
     "detail": "Article not found"
   }   
   ```

   ## Environment Variables

| Variable      | Description                 | Default Value                    |
|--------------|-----------------------------|----------------------------------|
| `MONGODB_URL` | MongoDB connection string   | `mongodb//srv`      |



   

   
   
      


