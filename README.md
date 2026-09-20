# Task Management API

A REST API for managing tasks and projects, built on top of Django REST Framework. It handles JWT auth, Redis caching, runs in Docker, and ships with full test coverage and Swagger docs.

---

## Features

- User Authentication (JWT)
- Project & Task Management (CRUD)
- Owner-based Permissions (secure access control)
- Filtering, Search & Ordering
- Redis Caching with Invalidation
- Docker & Docker Compose
- Automated Tests (pytest)
- Swagger / OpenAPI Documentation

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT (SimpleJWT)
- **Database:** PostgreSQL
- **Cache:** Redis
- **Docs:** drf-spectacular
- **Testing:** pytest pytest-django
- **Containerization:** Docker, Docker Compose

---

## Architecture Overview
Each user owns their own projects. Each project holds tasks. You can’t touch another user’s data — the queryset is scoped per user at every level.

Tasks have:
- Status: (`todo`, `in_progress`, `done`)
- Priority: (`low`, `medium`, `high`)
- Due dates
- An optional assignee

---

## Authentication

JWT-based authentication using **SimpleJWT**.

### Available Auth Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Obtain access & refresh tokens |
| POST | `/api/auth/token/refresh` | Refresh access token |

### Example: Login

```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "mahdi",
  "password": "StrongPass123!"
}
````

---

## API Endpoint

### Projects

| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| GET    | `/api/projects/`      | List user projects |
| POST   | `/api/projects/`      | Create project     |
| GET    | `/api/projects/{id}/` | Retrieve project   |
| PUT    | `/api/projects/{id}/` | Update project     |
| DELETE | `/api/projects/{id}/` | Delete project     |

### Tasks (Nested under projects)

| Method | Endpoint                              | Description   |
| ------ | ------------------------------------- | ------------- |
| GET    | `/api/projects/{id}/tasks/`           | List tasks    |
| POST   | `/api/projects/{id}/tasks/`           | Create task   |
| GET    | `/api/projects/{id}/tasks/{task_id}/` | Retrieve task |
| PUT    | `/api/projects/{id}/tasks/{task_id}/` | Update task   |
| DELETE | `/api/projects/{id}/tasks/{task_id}/` | Delete task   |

---

## Filtering, Search & Ordering

### Tasks Filtering

```
/api/projects/{id}/tasks/?status=todo
/api/projects/{id}/tasks/?priority=3
/api/projects/{id}/tasks/?due_date=2026-02-10
```

### Search

```
/api/projects/?search=workspace
/api/projects/{id}/tasks/?search=auth
```

### Ordering

```
/api/projects/{id}/tasks/?ordering=due_date
/api/projects/{id}/tasks/?ordering=-created_at
```

---

## API Docs

Swagger UI lives at GET `/api/swagger/` and the raw OpenAPI schema is at GET `/api/schema/`.

---

## Redis Caching

Project lists and task lists are cached per user and per query string. Any write operation (create, update, delete) automatically clears the relevant cache. Makes a noticeable difference on list-heavy usage.

---

## Running Locally

```bash
docker compose -f docker-compose.yml up --build
```

---

## Running Tests (Dockerized)

Tests run inside Docker to keep the environment consistent:

```bash
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit
docker compose -f docker-compose.test.yml down -v
```

### Covered:
* Authentication (register/login/token refresh)
* Permissions (owner-only access)
* Project CRUD
* Task CRUD
* Filtering and access control

---

## Security Considerations

* JWT Authentication
* Password validation enabled
* Owner-based permissions
* Access is controlled at the queryset level, not just the view
* Safe defaults for production settings

---

## Project Status

Core features are done and working. It’s Dockerized, cached, tested, and CI-ready. Next steps could include teams, role-based permissions, or notifications — the structure supports it.

---

## 👤 Author

**Seyyed Mahdi Sepahbodi**

Feel free to use this project as a base for more advanced task management systems.
