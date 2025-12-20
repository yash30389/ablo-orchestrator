# ---- Base image (stable & enterprise-safe) ----
FROM python:3.11-slim

# ---- Environment configuration ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Set working directory ----
WORKDIR /app

# ---- System dependencies (minimal) ----
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy dependency definition first (layer caching) ----
COPY pyproject.toml ./

# ---- Install Python dependencies ----
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -e .

# ---- Copy application source code ----
COPY src ./src
COPY docker ./docker

# ---- Expose API port ----
EXPOSE 8000

# ---- Run FastAPI application ----
CMD ["uvicorn", "ablo.apps.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

