from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    color: Optional[str] = Field(None, pattern="^#[0-9a-fA-F]{6}$")
    icon: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class EpochBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    color: Optional[str] = Field(None, pattern="^#[0-9a-fA-F]{6}$")

class EpochCreate(EpochBase):
    pass

class Epoch(EpochBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    location: Optional[str] = None
    importance: Optional[int] = Field(1, ge=1, le=5)
    media_url: Optional[str] = None
    epoch_id: int
    category_ids: List[int] = []

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    created_at: datetime
    updated_at: datetime
    epoch: Epoch
    categories: List[Category] = []

    class Config:
        from_attributes = True
