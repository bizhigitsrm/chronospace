import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

@pytest.mark.asyncio
async def test_database_tables():
    """Test that all required tables were created."""
    async for session in get_db():
        # Check for each table's existence
        tables = ["events", "categories", "epochs", "event_category"]
        for table in tables:
            result = await session.execute(text(f"SELECT 1 FROM {table} LIMIT 1"))
            # This will raise an error if the table doesn't exist
            result.scalar()
