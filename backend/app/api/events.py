from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.session import get_db
from ..db.crud import event, category, epoch
from ..schemas.event import (
    Event, EventCreate,
    Category, CategoryCreate,
    Epoch, EpochCreate
)

router = APIRouter()

# Event endpoints
@router.post("/events/", response_model=Event)
async def create_event(
    event_in: EventCreate,
    db: AsyncSession = Depends(get_db)
):
    return await event.create(db=db, obj_in=event_in)

@router.get("/events/", response_model=List[Event])
async def read_events(
    skip: int = 0,
    limit: int = 100,
    category_id: Optional[int] = None,
    epoch_id: Optional[int] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: AsyncSession = Depends(get_db)
):
    events = await event.get_multi(
        db,
        skip=skip,
        limit=limit,
        category_id=category_id,
        epoch_id=epoch_id,
        start_date=start_date,
        end_date=end_date
    )
    return events

@router.get("/events/{event_id}", response_model=Event)
async def read_event(event_id: int, db: AsyncSession = Depends(get_db)):
    db_event = await event.get(db=db, id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.delete("/events/{event_id}")
async def delete_event(event_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await event.delete(db=db, id=event_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"status": "success"}

# Category endpoints
@router.post("/categories/", response_model=Category)
async def create_category(
    category_in: CategoryCreate,
    db: AsyncSession = Depends(get_db)
):
    db_category = await category.get_by_name(db=db, name=category_in.name)
    if db_category:
        raise HTTPException(
            status_code=400,
            detail="Category with this name already exists"
        )
    return await category.create(db=db, obj_in=category_in)

@router.get("/categories/", response_model=List[Category])
async def read_categories(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    categories = await category.get_multi(db, skip=skip, limit=limit)
    return categories

@router.get("/categories/{category_id}", response_model=Category)
async def read_category(category_id: int, db: AsyncSession = Depends(get_db)):
    db_category = await category.get(db=db, id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/categories/{category_id}")
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await category.delete(db=db, id=category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"status": "success"}

# Epoch endpoints
@router.post("/epochs/", response_model=Epoch)
async def create_epoch(
    epoch_in: EpochCreate,
    db: AsyncSession = Depends(get_db)
):
    db_epoch = await epoch.get_by_name(db=db, name=epoch_in.name)
    if db_epoch:
        raise HTTPException(
            status_code=400,
            detail="Epoch with this name already exists"
        )
    return await epoch.create(db=db, obj_in=epoch_in)

@router.get("/epochs/", response_model=List[Epoch])
async def read_epochs(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    epochs = await epoch.get_multi(db, skip=skip, limit=limit)
    return epochs

@router.get("/epochs/{epoch_id}", response_model=Epoch)
async def read_epoch(epoch_id: int, db: AsyncSession = Depends(get_db)):
    db_epoch = await epoch.get(db=db, id=epoch_id)
    if db_epoch is None:
        raise HTTPException(status_code=404, detail="Epoch not found")
    return db_epoch

@router.delete("/epochs/{epoch_id}")
async def delete_epoch(epoch_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await epoch.delete(db=db, id=epoch_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Epoch not found")
    return {"status": "success"}
