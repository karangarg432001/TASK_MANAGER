# Task Manager Application

## Overview

The Task Manager Application is a Django-based web application designed to help users manage their tasks efficiently. It provides features such as user authentication, task creation, updating, and deletion.

## Technologies Used:

- **Backend:** Django (Python web framework)
- **Database:** SQLite (for development) / MySQL (for production)
- **Frontend:** Django Templates (HTML with Django template language)
- **Authentication:** Django's built-in JWT authentication system with token-based authentication
- **Testing:** Django's testing framework for unit and integration tests
- **Deployment:** Docker for containerization and easy deployment

## Features:

- **User Authentication:**: Users can register, log in, and log out securely. Authentication is handled using tokens to ensure secure communication between the client and server.
- **Task Management:** Users can create, update, and delete tasks. Each task includes details such as title, description, completion status, and timestamps for creation and last update.
- **User-specific Views:** Users can only view and manage tasks that they have created. Tasks are associated with the user who created them, ensuring data privacy and security.
- **Admin Functionality:** Administrators have access to additional features such as viewing all tasks, managing user accounts, and performing administrative tasks.

## Setup Instructions

Follow these steps to set up and run the Task Manager Application:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd task-manager
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv env
source env/bin/activate  # For Unix/Linux
env\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Perform Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be accessible at `http://localhost:8000`.

## Additional Notes

- **Authentication:** The application uses JWT token-based authentication. Users can obtain tokens by logging in or registering using login and register API's.
- **API Endpoints:** The application provides RESTful API endpoints for tasks management. These endpoints can be accessed programmatically by clients.
- **Testing:** Unit tests are included in the `tasks/tests.py` file. You can run tests using the following command:

```bash
python manage.py test tasks
python manage.py test --keepdb tasks # For Saving test database
```

- **Docker:** The application can also be containerized using Docker. A Dockerfile and docker-compose.yml file are provided for this purpose.

## Setup Instructions using Docker:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd task-manager
```

### 2. Build and Run with Docker Compose

```bash
docker-compose -f docker-compose.yml up --build -d
```

This command will build the Docker images for the application and its dependencies, create containers, and start the services.

The application will be accessible at `http://localhost:8000`.

### 3. Perform Database Migrations

If this is the first time running the application or if there are changes to the database schema, perform the following steps:

```bash
docker exec -it task_manager python3 manage.py makemigrations
docker exec -it task_manager python3 manage.py migrate
```

### 4. Create a Superuser (Admin)

To access the Django Admin interface and have administrative privileges, create a superuser:

```bash
docker  exec -it task_manager python3 manage.py createsuperuser
```


### 5. Testing: Unit tests are included in the `tasks/tests.py` file. You can run tests using the following command:

```bash
docker exec -it  task_manager python3 manage.py test tasks
```

- [Karan Aggarwal](https://github.com/karangarg432001)

Feel free to contribute by submitting bug reports, feature requests, or pull requests.