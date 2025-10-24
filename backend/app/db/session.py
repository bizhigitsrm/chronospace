from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import os

from ..core.config import settings

# Use SQLite for testing if DATABASE_URL is set
database_url = os.getenv("DATABASE_URL", settings.SQLALCHEMY_DATABASE_URI)
engine = create_async_engine(
    database_url,
    echo=True,
    future=True
)

# Create async session factory with async_sessionmaker
async_session_factory = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async database sessions."""
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()
