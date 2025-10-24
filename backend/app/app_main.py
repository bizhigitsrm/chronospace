from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import events

# Support both package-relative imports (production) and absolute imports
# when tests run with PYTHONPATH pointing to backend/app.
try:
    from .core.config import settings
    from .api import events
except Exception:
    # Fallback to absolute imports when module is loaded as top-level
    from core.config import settings  # type: ignore
    from api import events  # type: ignore


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events.router, prefix=settings.API_V1_STR)


@app.get("/", tags=["meta"])
async def root():
    return {"project": settings.PROJECT_NAME, "api": settings.API_V1_STR}


@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok"}
