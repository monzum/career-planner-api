# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install -y curl \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean


# Copy application code
COPY app ./app

# Default port (can be overridden at runtime)
ENV PORT=8000

# Expose the port
EXPOSE ${PORT}

# Healthcheck to verify container is running properly
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${PORT}/health || exit 1


# Start FastAPI using the environment variable
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
