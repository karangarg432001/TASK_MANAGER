# Use official Python image as base
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install SQLite
RUN apt-get update && \
    apt-get install -y sqlite3 && \
    rm -rf /var/lib/apt/lists/*
    
# Set working directory
WORKDIR /task_manager

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
