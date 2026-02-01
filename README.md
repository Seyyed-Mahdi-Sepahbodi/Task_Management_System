# 🗂️ Task Management API

A production-ready **Task Management REST API** built with **Django Rest Framework**, featuring JWT authentication, Redis caching, Dockerized setup, automated tests, and swagger documentation.

This project is designed with **clean architecture**, **real-world permissions**, and **scalability** in mind.

---

## ✨ Features

- ✅ User Authentication (JWT)
- ✅ Project & Task Management (CRUD)
- ✅ Owner-based Permissions (secure access control)
- ✅ Advanced Filtering, Search & Ordering
- ✅ Redis Caching with Invalidation
- ✅ Docker & Docker Compose
- ✅ Automated Tests (pytest)
- ✅ CI-ready setup
- ✅ Swagger / OpenAPI Documentation

---

## 🏗️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT (SimpleJWT)
- **Database:** PostgreSQL
- **Cache:** Redis
- **Docs:** drf-spectacular (Swagger / OpenAPI)
- **Testing:** pytest pytest-django
- **Containerization:** Docker, Docker Compose

---

## 📐 Architecture Overview

- Each **User** owns multiple **Projects**
- Each **Project** contains multiple **Tasks**
- User can only access **their own projects and tasks**
- Task support:
  - status (`todo`, `in_progress`, `done`)
  - priority (`low`, `medium`, `high`)
  - due dates
  - optional assignee

---

## 🔐 Authentication

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

## 📁 API Endpoint

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

## 🔍 Filtering, Search & Ordering

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

## 🚀 Swagger / API Documentation

Swagger UI is enabled via **drf-spectacular**.

* Swagger UI:
  👉 `GET /api/swagger/`

* OpenAPI schema:
  👉 `GET /api/schema/`

---

## ⚡ Redis Caching

* Cached endpoints:
  * Porject list per user
  * Task list per project
* Cache keys are user-aware and query-aware
* Automatic cache invalidation on:
  * create
  * update
  * delete

This significantly improves performance for list-heavy endpoints.

---

## 🐳 Docker Setup

### Development Environment

```bash
docker compose -f docker-compose.yml up --build
```

---

## 🧪 Running Tests (Dockerized)

Tests run **inside Docker Compose**, ensuring consistency across environments.

```bash
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit
docker compose -f docker-compose.test.yml down -v
```

### Test Coverage Includes

* Authentication (register/login/refresh)
* Permissions (owner-only access)
* Project CRUD
* Task CRUD
* Filtering & access control

---

## 🧠 Security Considerations

* JWT Authentication
* Password validation enabled
* Owner-based permissions
* Queryset-level access control
* Safe defaults for production settings

---

## 📦 Environment Variables

Example `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=taskdb
DB_USER=taskuser
DB_PASSWORD=taskpass
DB_HOST=db
DB_PORT=5432

REDIS_URL=redis://redis:6379/1
```

---

## 📌 Project Status

✅ Core features completed
✅ Dockerized
✅ Cached & optimized
✅ Tested & CI-ready
🚀 Ready for extension (teams, roles, notifications, etc.)

---

## 📄 License

This project is open-source and intended for educational and portfolio purposes.

---

## 👤 Author

**Seyyed Mahdi Sepahbodi**

Feel free to use this project as a base for more advanced task management systems.
