from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class ArticleStatus(str, Enum):
    draft = "draft"
    published = "published"


class ArticleCategory(str, Enum):
    mining = "mining"
    crypto = "crypto"


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
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    publishDate: Optional[datetime] = None
    status: Optional[ArticleStatus] = None
    category: Optional[ArticleCategory] = None


class ArticleResponse(ArticleBase):
    id: str
    createdAt: datetime
    updatedAt: datetime
