# Use the official Python image as base
FROM python:3.9-slim

# Set environment variables
ENV POST_DB_USERNAME=postgres
ENV POST_DB_PASSWORD=0707
ENV HOST_IP_ADR=172.21.224.1
ENV DB_PORT=5432
ENV POST_DB_NAME=otter_post_database

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5002

# Command to run the Flask app
CMD ["python", "post_microservice.py"]
