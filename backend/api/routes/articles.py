from fastapi import APIRouter, HTTPException, status
from db.database import collection
from schemas.article import ArticleCreate, ArticleUpdate, ArticleResponse
from fastapi.responses import Response
from bson import ObjectId
from datetime import datetime
import logging
from uuid import uuid4

logger = logging.getLogger(__name__)

router = APIRouter()


def article_helper(article) -> dict:
    """Convert MongoDB document to API-friendly format"""
    return {"id": str(article["_id"]), **{k: v for k, v in article.items() if k != "_id"}}


@router.get("/", response_model=list[ArticleResponse])
async def list_articles(skip: int = 0, limit: int = 10):
    articles = [article_helper(article)
                for article in collection.find().skip(skip).limit(limit)]
    return articles


@router.post("/", response_model=ArticleResponse, status_code=status.HTTP_201_CREATED)
async def create_article(article: ArticleCreate):
    try:
        article_data = article.dict()
        article_data["id"] = str(uuid4())
        article_data["createdAt"] = datetime.utcnow()
        article_data["updatedAt"] = datetime.utcnow()
        collection.insert_one(article_data)
        return article_helper(article_data)
    except Exception as e:
        logger.error(f"Error creating article: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create article")


@router.get("/{article_id}", response_model=ArticleResponse)
async def get_article(article_id: str):
    article = collection.find_one({"id": article_id})
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article_helper(article)


@router.put("/{article_id}", response_model=ArticleResponse)
async def update_article(article_id: str, article: ArticleUpdate):
    update_data = article.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=400, detail="No valid update data provided")

    update_data["updatedAt"] = datetime.utcnow()
    result = collection.update_one({"id": article_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Article not found")

    updated_article = collection.find_one({"id": article_id})
    return article_helper(updated_article)


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_id: str):
    result = collection.delete_one({"id": article_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Article not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
