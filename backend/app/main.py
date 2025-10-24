"""Application entry wrapper.

This file provides a safe `app` symbol for uvicorn invocation like
`uvicorn backend.app.main:app` (when running from repo root) or
`uvicorn main:app` when running inside the `backend/app` folder.

We forward to the clean `app_main.py` created for CI/tests.
"""

try:
    # When imported as package (recommended)
    from .app_main import app
except Exception:
    # When run from the app directory directly
    try:
        from app_main import app
    except Exception:
        # Fallback to minimal app to avoid import errors in some environments
        from fastapi import FastAPI

        app = FastAPI()
