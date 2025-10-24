"""Backend application package initializer.

This file makes `backend/app` importable as a package which stabilizes
relative imports during tests, CI and when running via uvicorn.
"""

__all__ = ["app_main", "api", "db", "core", "schemas"]
