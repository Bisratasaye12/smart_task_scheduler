
# Smart Task Scheduler

## Overview

Smart Task Scheduler is a web application that allows users to create, manage, and delete tasks efficiently. Built with Flask, this application integrates with Amazon DynamoDB for seamless data storage and retrieval, enabling high scalability and low latency. This project showcases modern web development practices, including authentication, middleware, and clean architecture.

## Features

- **User Authentication**: Secure user registration and login using JWT tokens.
- **Task Management**: Create, read, update, and delete (CRUD) tasks associated with authenticated users.
- **DynamoDB Integration**: Utilizes Amazon DynamoDB as the primary database for storing tasks and user information, offering flexible schema and high availability.
- **Middleware Implementation**: Token verification middleware to ensure secure access to routes.

## Tech Stack

- **Backend**: Flask
- **Database**: Amazon DynamoDB
- **Authentication**: JWT (JSON Web Tokens)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- DynamoDB (local instance)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/smart_task_scheduler.git
   cd smart_task_scheduler
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your DynamoDB locally by following the [official documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html).

### Running the Application

1. Start the Flask application:

   ```bash
   python run.py
   ```

2. The application will be accessible at `http://127.0.0.1:5000`.

### API Endpoints

- **User Authentication**
  - `POST /auth/register`: Register a new user.
  - `POST /auth/login`: Login and receive a JWT token.

- **Task Management**
  - `POST /api/v1/tasks`: Create a new task.
  - `GET /api/v1/tasks/<task_id>`: Retrieve a specific task.
  - `GET /api/v1/tasks`: Retrieve all tasks for the authenticated user.
  - `PUT /api/v1/tasks/<task_id>`: Update an existing task.
  - `DELETE /api/v1/tasks/<task_id>`: Delete a specific task.

### Middleware

The application implements token verification as middleware to protect routes. Users must include the JWT token in the `Authorization` header when accessing secured endpoints.

### Models

- **User Model**: Represents the user entity with fields like `user_id`, `username`, and `password`.
- **Task Model**: Represents the task entity with fields like `task_id`, `user_id`, `title`, `description`, and `status`.

### Using DynamoDB

DynamoDB is a fully managed NoSQL database service provided by AWS. In this application:

- Each user and their associated tasks are stored in separate tables (`Users` and `Tasks`).
- The use of `scan` and `get_item` operations allows for efficient data retrieval.
- The application leverages DynamoDB’s scalability features to handle varying loads without compromising performance.

## Acknowledgments

- Flask documentation for building web applications.
- AWS DynamoDB documentation for understanding data modeling and querying.

## Postman published documentation

[Postman documentation](https://documenter.getpostman.com/view/32287741/2sAY4vi3YB)
```

