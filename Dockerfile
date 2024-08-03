# Start from a Python base image
FROM python:3.12.3-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of your application's code
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask application using Gunicorn for production
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:5000", "app:app"]