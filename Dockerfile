# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Default port (can be overridden at runtime)
ENV PORT=8000

# Expose the port
EXPOSE ${PORT}

# Start FastAPI using the environment variable
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
