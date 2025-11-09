# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 8080
EXPOSE 8080

# Set environment variable
ENV PORT=8080

# Run the application
CMD ["python", "app.py"]

