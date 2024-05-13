# Use the official Python image as base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Install dependencies
COPY ../requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code into the container
COPY .. /app/

# Expose port 8001 (or any other port you're using)
EXPOSE 8001

# Command to run the Flask app
CMD ["python", "user_microservice.py"]
