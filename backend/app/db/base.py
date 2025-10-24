from typing import Any

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    """Base class for all database models."""

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
