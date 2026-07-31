# Task API (SQLite)

## Overview

This project is a CRUD Task API built with FastAPI and SQLite.

The API supports:

- Create Task
- Get All Tasks
- Get Task by ID
- Update Task
- Delete Task

Unlike the previous assignment, tasks are stored inside a SQLite database instead of an in-memory list.

---

## Technologies Used

- Python
- FastAPI
- SQLite
- sqlite3
- Pydantic
- Uvicorn

---

## Project Structure

```
CRUD_API/
│
├── main.py
├── tasks.db
├── requirements.txt
├── README.md
└── database.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/HafizMuhammadAsim/CRUD_API.git
```

Go to project folder:

```bash
cd CRUD_API
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Root |
| GET | /health | Health Check |
| GET | /tasks | Get All Tasks |
| GET | /tasks/{id} | Get Task by ID |
| POST | /tasks | Create Task |
| PUT | /tasks/{id} | Update Task |
| DELETE | /tasks/{id} | Delete Task |

---

## Example SQL Queries

```sql
SELECT * FROM tasks;
```

```sql
SELECT * FROM tasks WHERE done = 1;
```

```sql
SELECT COUNT(*) FROM tasks;
```

---

## Database Screenshot

The SQLite database screenshot is included.

Filename:

```
database.png
```

---

## Author

**Hafiz Muhammad Asim**

Backend AI Engineering Internship – Week 3 Assignment