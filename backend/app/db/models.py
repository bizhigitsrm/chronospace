from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

# Association table for many-to-many relationship between events and categories
event_category = Table(
    'event_category',
    Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    date = Column(DateTime, nullable=False)
    location = Column(String(255))
    importance = Column(Integer, default=1)  # Scale 1-5
    media_url = Column(String(512))  # URL to image/video
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    epoch_id = Column(Integer, ForeignKey('epochs.id'))
    epoch = relationship("Epoch", back_populates="events")
    categories = relationship("Category", secondary=event_category, back_populates="events")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    color = Column(String(7))  # Hex color code
    icon = Column(String(100))  # Icon identifier
    created_at = Column(DateTime, default=datetime.utcnow)

    events = relationship("Event", secondary=event_category, back_populates="categories")

class Epoch(Base):
    __tablename__ = "epochs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    color = Column(String(7))  # Hex color code
    created_at = Column(DateTime, default=datetime.utcnow)

    events = relationship("Event", back_populates="epoch")
