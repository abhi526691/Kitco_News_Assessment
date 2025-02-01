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

3. Set up environment variables:
   Create a .env file in the root directory:
   ```bash
   MONGODB_URL=mongodb+srv://username:password.qdpo3.mongodb.net/db_name?retryWrites=true&w=majority&appName=speer
   ```
