# Use official slim Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install minimal build deps for some Python packages (optional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose Django default port
EXPOSE 8000

# Environment defaults (override these at runtime for production)
ENV DJANGO_SETTINGS_MODULE=messaging_app.settings
ENV PORT=8000

# Run migrations then run the dev server (in production replace with gunicorn)
CMD python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput || true && \
    python manage.py runserver 0.0.0.0:8000
