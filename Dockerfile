# Use Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make sure the apple_intelligence package is in the Python path
ENV PYTHONPATH=/app

# Command to run the application
CMD ["adk", "web"]
