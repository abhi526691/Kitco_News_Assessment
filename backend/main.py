from uuid import uuid4  # Import uuid4 from the uuid library
from uuid import uuid4
from datetime import datetime
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel, validator
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from typing import Optional, List
import logging
import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB configuration
MONGODB_URL = os.getenv("mongo_url")
DB_NAME = "articles_db"
COLLECTION_NAME = "articles"

# Connect to MongoDB
client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Create indexes
# collection.create_index("id", unique=True)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add security headers middleware


@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

# Request/Response logging middleware


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise
    logger.info(f"Response status: {response.status_code}")
    return response

# Enums


class ArticleStatus(str, Enum):
    draft = "draft"
    published = "published"


class ArticleCategory(str, Enum):
    mining = "mining"
    crypto = "crypto"

# Pydantic models


class ArticleBase(BaseModel):
    title: str
    content: str
    author: str
    publishDate: datetime
    status: ArticleStatus
    category: ArticleCategory


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(BaseModel):
    """Model for article updates with optional fields"""
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    publishDate: Optional[datetime] = None
    status: Optional[ArticleStatus] = None
    category: Optional[ArticleCategory] = None


class Article(ArticleBase):
    """Complete article model including system-generated fields"""
    id: str
    createdAt: datetime
    updatedAt: datetime

    @validator("id", pre=True)
    def validate_id(cls, v):
        return str(v)

# Helper functions


def article_helper(article) -> dict:
    """Convert MongoDB document to API-friendly format"""
    return {
        "id": str(article["_id"]),
        **{k: v for k, v in article.items() if k != "_id"}
    }

# Routes


@app.get("/articles", response_model=List[Article], status_code=status.HTTP_200_OK)
async def list_articles(skip: int = 0, limit: int = 10):
    """
    Retrieve paginated list of articles

    Parameters:
    - skip: Number of items to skip (for pagination)
    - limit: Maximum number of items to return

    Returns:
    - List of Article objects with pagination
    """
    articles = []
    for article in collection.find().skip(skip).limit(limit):
        articles.append(article_helper(article))
    return articles


@app.post("/articles", response_model=Article, status_code=status.HTTP_201_CREATED)
async def create_article(article: ArticleCreate):
    """
    Create a new article with a unique UUID.
    """
    try:
        # Generate a unique ID
        article_id = str(uuid4())

        # Convert Pydantic model to dictionary
        article_data = article.dict()

        # Add system-generated fields
        now = datetime.utcnow()
        article_data.update({
            "id": article_id,  # Add the generated ID
            "createdAt": now,
            "updatedAt": now
        })

        # Insert into MongoDB
        result = collection.insert_one(article_data)

        # Fetch the newly created document
        created_article = collection.find_one({"_id": result.inserted_id})

        # Return the created article
        return article_helper(created_article)

    except DuplicateKeyError as e:
        # Handle duplicate key error (unlikely with UUIDs)
        logger.error(f"Duplicate key error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Article with the same ID already exists"
        )
    except Exception as e:
        # Handle other errors
        logger.error(f"Error creating article: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create article"
        )


@app.get(
    "/articles/{article_id}",
    response_model=Article,
    summary="Get a single article by ID",
    description="Retrieve a single article by its unique ID.",
    responses={
        200: {"description": "Article retrieved successfully"},
        400: {"description": "Invalid ID format"},
        404: {"description": "Article not found"},
        500: {"description": "Internal server error"}
    }
)
async def get_article(article_id: str):
    """
    Get a single article by ID.

    Parameters:
    - **article_id**: Unique ID of the article to retrieve.

    Returns:
    - **Article**: The complete article object.

    Raises:
    - **HTTPException 400**: If the provided ID is invalid.
    - **HTTPException 404**: If no article is found with the given ID.
    - **HTTPException 500**: If there is a database error.
    """
    try:
        # Log the request
        logger.info(f"Fetching article with ID: {article_id}")

        # Find the article by the custom 'id' field
        article = collection.find_one({"id": article_id})

        # If article is not found, raise 404 error
        if article is None:
            logger.warning(f"Article not found: {article_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with ID '{article_id}' not found"
            )

        # Return the article
        logger.info(f"Successfully fetched article: {article_id}")
        return article_helper(article)

    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error fetching article {article_id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching the article"
        )


@app.put(
    "/articles/{article_id}",
    response_model=Article,
    summary="Update an existing article",
    description="Update specific fields of an existing article by its unique ID.",
    responses={
        200: {"description": "Article updated successfully"},
        400: {"description": "Invalid update data or ID format"},
        404: {"description": "Article not found"},
        500: {"description": "Internal server error"}
    }
)
async def update_article(article_id: str, article: ArticleUpdate):
    """
    Update an existing article.

    Parameters:
    - **article_id**: Unique ID of the article to update.
    - **article**: ArticleUpdate object containing fields to modify.

    Returns:
    - **Article**: The updated article object.

    Raises:
    - **HTTPException 400**: If no valid update data is provided.
    - **HTTPException 404**: If no article is found with the given ID.
    - **HTTPException 500**: If there is a database error.
    """
    try:
        # Log the request
        logger.info(f"Updating article with ID: {article_id}")

        # Convert update data to dictionary and exclude unset fields
        update_data = article.dict(exclude_unset=True)

        # If no valid update data is provided, raise 400 error
        if not update_data:
            logger.warning("No valid update data provided")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No valid update data provided"
            )

        # Add updatedAt timestamp
        update_data["updatedAt"] = datetime.utcnow()

        # Perform the update operation
        result = collection.update_one(
            {"id": article_id},  # Use the custom 'id' field
            {"$set": update_data}
        )

        # If no document was modified, raise 404 error
        if result.matched_count == 0:
            logger.warning(f"Article not found: {article_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with ID '{article_id}' not found"
            )

        # Fetch the updated document
        updated_article = collection.find_one({"id": article_id})
        if updated_article is None:
            logger.error(f"Article fetch failed after update: {article_id}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch updated article"
            )

        # Log success and return the updated article
        logger.info(f"Successfully updated article: {article_id}")
        return article_helper(updated_article)

    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error updating article {article_id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating the article"
        )


@app.delete(
    "/articles/{article_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an article",
    description="Delete an existing article by its unique ID.",
    responses={
        204: {"description": "Article deleted successfully"},
        400: {"description": "Invalid ID format"},
        404: {"description": "Article not found"},
        500: {"description": "Internal server error"}
    }
)
async def delete_article(article_id: str):
    """
    Delete an existing article.

    Parameters:
    - **article_id**: Unique ID of the article to delete.

    Returns:
    - **204 No Content**: If the article is successfully deleted.

    Raises:
    - **HTTPException 400**: If the provided ID is invalid.
    - **HTTPException 404**: If no article is found with the given ID.
    - **HTTPException 500**: If there is a database error.
    """
    try:
        # Log the request
        logger.info(f"Deleting article with ID: {article_id}")

        # Perform the delete operation
        delete_result = collection.delete_one(
            {"id": article_id})  # Use the custom 'id' field

        # If no document was deleted, raise 404 error
        if delete_result.deleted_count == 0:
            logger.warning(f"Article not found: {article_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with ID '{article_id}' not found"
            )

        # Log success and return 204 No Content
        logger.info(f"Successfully deleted article: {article_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error deleting article {article_id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting the article"
        )
