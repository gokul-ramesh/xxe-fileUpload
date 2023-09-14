# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE XXE_fileUpload.settings

# Create and set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django development server when the container runs
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
