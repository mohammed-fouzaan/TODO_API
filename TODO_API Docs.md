# Django REST Framework TODO App API Documentation

## Introduction

This documentation provides instructions on how to set up and use the Django REST Framework API for a TODO App. The API includes endpoints for tasks, login, logout, and register. It enforces strong authentication and authorization mechanisms to ensure data security and user-specific access.

- **API Base URL**: `http://127.0.0.1:8000/`

## Endpoints

### 1. Tasks Endpoint

- **URL**: `/tasks/`
- **Description**: This endpoint allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks. Users can only access and manipulate tasks they have created.

#### Example Task JSON Output Structure
This is the example output for a tasks `GET` API call.
```json
{
    "id": 1,
    "title": "Sample Task",
    "description": "This is a sample task description.",
    "duedate": "31/10/2023",
    "priority": "High",
    "progress": "Completed",
    "created": "28/10/2023 14:00:00",
    "updated": "30/10/2023 13:50:20"
}
```

### 2. Authentication Endpoints

#### a. Register

- **URL**: `/register/`
- **Description**: Register a new user with a unique username and password.

#### b. Login

- **URL**: `/login/`
- **Description**: Authenticate and obtain an access token for accessing secured endpoints.

#### c. Logout

- **URL**: `/logout/`
- **Description**: Logout and invalidate the access token.

## Setting Up the API

1. Clone the repository:

   ```bash
   git clone https://github.com/mohammed-fouzaan/TODO_API
   cd TODO_API
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create the database and apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser for admin access and manual database management at `http://127.0.0.1:8000/admin/`:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/`.

## Usage
The API can be used along with any frontend framework for a robust and secure TODO list management app. The Following are some Example API calls using curl:
### Registration

To register a new user, make a `POST` request to the `/register/` endpoint:

```bash
curl -X POST -d "username=<username>&password=<password>" http://127.0.0.1:8000/register/
```

### Login

To log in and obtain an access token, make a `POST` request to the `/login/` endpoint:

```bash
curl -X POST -d "username=<username>&password=<password>" http://127.0.0.1:8000/login/
```

On a succesful login the response will provide a access token as given below.
```json
{"message":"Login successful","sessionid":<sessionid>,"csrftoken":<csrftoken>}
```
### Logout

To log out and invalidate the access token, make a blank `POST` request to the `/logout/` endpoint:

```bash
curl -X POST -d "" http://127.0.0.1:8000/logout/
```
#### Ouput on successful Logout
```json
{'message': 'Logout successful'}
```
### Task Operations

To perform CRUD operations on tasks, you need to provide the access token in the request header for authentication.

- Create a new task (POST):

To add a new task to the database:
  ```bash
  curl -X POST -H "Cookie: sessionid=<session_id>; csrftoken=<csrftoken>" -d "title=Task Title&description=Task Description&duedate=2023-12-31&priority=High" http://127.0.0.1:8000/tasks/
  ```

- Retrieve a list of tasks (GET):

To retrieve a list of all tasks from the database specific to the user logged in:
  ```bash
  curl -H "Cookie: sessionid=<session_id>; csrftoken=<csrftoken>" http://127.0.0.1:8000/tasks/
  ```
Example Output:
```json
[{  "id": 1,
    "title": "Sample Task",
    "description": "This is a sample task description.",
    "duedate": "31/10/2023",
    "priority": "High",
    "progress": "Completed",
    "created": "28/10/2023 14:00:00",
    "updated": "30/10/2023 13:50:20"}
    {"id": 2,
    "title": "Sample Task 2",
    "description": "This is a sample task description.",
    "duedate": "31/10/2023",
    "priority": "Low",
    "progress": "To Do"
    "created": "28/10/2023 14:00:00",
    "updated": "30/10/2023 13:50:20"}]
```
- Retrieve a specific task (GET):

To retrieve a specific requested task from the database:
  ```bash
  curl -H "Cookie: sessionid=<session_id>; csrftoken=<csrftoken>" http://127.0.0.1:8000/tasks/<task_id>/
  ```
Example output:
```json
[{
    "id": 1,
    "title": "Sample Task",
    "description": "This is a sample task description.",
    "duedate": "31/10/2023",
    "priority": "High",
    "progress": "Completed",
    "created": "28/10/2023 14:00:00",
    "updated": "30/10/2023 13:50:20"
}]
```
- Update a task (PUT or PATCH):

To Update a specific task from the database:
  ```bash
  curl -X PUT -H "Cookie: sessionid=<session_id>; csrftoken=<csrftoken>" -d "title=New Title" http://127.0.0.1:8000/tasks/<task_id>/
  ```

- Delete a task (DELETE):

To Delete a given task from the database:
  ```bash
  curl -X DELETE -H "Cookie: sessionid=<session_id>; csrftoken=<csrftoken>" http://127.0.0.1:8000/tasks/<task_id>/
  ```

## Security

The API enforces strong authentication mechanisms, ensuring that users can only access and modify their own tasks. Access tokens are required for most endpoints, and sessions are terminated with the `/logout/` endpoint.

## Conclusion

The Django REST Framework TODO App API provides a secure and efficient way to manage tasks with user-specific access controls. You can add, view, update, and delete tasks while ensuring security and privacy of the users data.

### Task Priority Levels

The API supports the following task priority levels:
- `Low`
- `Medium`
- `High`

When creating or updating a task, you can set the `priority` field to one of these values.

### Task Progress Status

The API supports the following task progress statuses:
- `To Do`
- `In Progress`
- `Completed`

When creating or updating a task, you can set the `progress` field to one of these values.
### Authentication and Authorization

The API uses token-based authentication for user access control. Users need to obtain an access token by logging in and use it for authorized access to the `/tasks/` endpoint.

### Date and Time Stamps

Each task includes two timestamp fields:
- `created_at`: Indicates when the task was created.
- `updated_at`: Shows the last time the task was updated.

These timestamps provide visibility into when a task was created and when it was last modified.

### Error Handling

The API provides detailed error responses in case of invalid requests, missing fields, or unauthorized access. Be sure to check the response status and message for troubleshooting.

### Best Practices

- Always protect your access token. Do not share it or include it in public scripts or URLs.
- Consider using HTTPS to secure communication with the API in a production environment.

## Summary

The Django REST Framework TODO App API offers a secure and flexible solution for managing tasks with strong user authentication and authorization. By following the setup instructions and using the provided examples, you can efficiently create, retrieve, update, and delete tasks while ensuring the privacy and security of user data.

If you encounter any issues or have questions about the API, please refer to the API documentation.