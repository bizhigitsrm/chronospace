from datetime import datetime
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import relationship, Mapped, mapped_column
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

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location: Mapped[str] = mapped_column(String(255))
    importance: Mapped[int] = mapped_column(default=1)  # Scale 1-5
    media_url: Mapped[str] = mapped_column(String(512))  # URL to image/video
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    epoch_id: Mapped[int] = mapped_column(ForeignKey('epochs.id'))
    epoch = relationship("Epoch", back_populates="events")
    categories = relationship("Category", secondary=event_category, back_populates="events")

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text)
    color: Mapped[str] = mapped_column(String(7))  # Hex color code
    icon: Mapped[str] = mapped_column(String(100))  # Icon identifier
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    events = relationship("Event", secondary=event_category, back_populates="categories")

class Epoch(Base):
    __tablename__ = "epochs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    color: Mapped[str] = mapped_column(String(7))  # Hex color code
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    events = relationship("Event", back_populates="epoch")
