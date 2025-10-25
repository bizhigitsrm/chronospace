# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  build-essential \
  libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY ./req.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r req.txt

# Copy application code
COPY . .

# Command to run the application
CMD ["uvicorn", "app_main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
