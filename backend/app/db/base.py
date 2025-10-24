from typing import Any

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for all database models."""

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
