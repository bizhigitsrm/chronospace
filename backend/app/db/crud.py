from datetime import datetime
from typing import List, Optional, Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..db.models import Event, Category, Epoch
from ..schemas.event import EventCreate, CategoryCreate, EpochCreate

class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get(self, db: AsyncSession, id: int):
        result = await db.execute(
            select(self.model).where(self.model.id == id)
        )
        return result.scalar_one_or_none()

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> List[Any]:
        result = await db.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    async def create(self, db: AsyncSession, *, obj_in: Any) -> Any:
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, *, id: int) -> bool:
        obj = await self.get(db, id)
        if obj:
            await db.delete(obj)
            await db.commit()
            return True
        return False

class CRUDEvent(CRUDBase):
    async def create(self, db: AsyncSession, *, obj_in: EventCreate) -> Event:
        # Get categories
        category_ids = obj_in.category_ids
        obj_data = obj_in.dict(exclude={'category_ids'})

        # Create event
        db_obj = Event(**obj_data)

        # Add categories
        if category_ids:
            categories = await db.execute(
                select(Category).where(Category.id.in_(category_ids))
            )
            db_obj.categories = categories.scalars().all()

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_multi(
        self,
        db: AsyncSession,
        *,
        skip: int = 0,
        limit: int = 100,
        category_id: Optional[int] = None,
        epoch_id: Optional[int] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Event]:
        query = select(Event).options(
            selectinload(Event.categories),
            selectinload(Event.epoch)
        )

        if category_id:
            query = query.join(Event.categories).filter(Category.id == category_id)
        if epoch_id:
            query = query.filter(Event.epoch_id == epoch_id)
        if start_date:
            query = query.filter(Event.date >= start_date)
        if end_date:
            query = query.filter(Event.date <= end_date)

        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

class CRUDCategory(CRUDBase):
    async def get_by_name(self, db: AsyncSession, name: str) -> Optional[Category]:
        result = await db.execute(
            select(Category).where(Category.name == name)
        )
        return result.scalar_one_or_none()

class CRUDEpoch(CRUDBase):
    async def get_by_name(self, db: AsyncSession, name: str) -> Optional[Epoch]:
        result = await db.execute(
            select(Epoch).where(Epoch.name == name)
        )
        return result.scalar_one_or_none()

# Create CRUD instances
event = CRUDEvent(Event)
category = CRUDCategory(Category)
epoch = CRUDEpoch(Epoch)
