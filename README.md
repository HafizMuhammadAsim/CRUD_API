# Task API (SQLite)

## Overview

This project is a CRUD Task API built with FastAPI and SQLite.

The API allows you to:

- Create tasks
- Read all tasks
- Read a single task
- Update tasks
- Delete tasks

Unlike the previous assignment, tasks are now stored in a SQLite database, so the data remains available even after restarting the server.

---

## Why SQLite?

SQLite was chosen because:

- It is lightweight.
- It requires no separate server.
- The database is stored in a single file.
- It is easy to use for small backend projects.

---

## Database Location

The database file is:

```
tasks.db
```

It is automatically created inside the project folder when the application starts.

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the server

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Example SQL Query

```sql
SELECT * FROM tasks;
```

This query returns every task stored in the database.

---

## Database Screenshot

A screenshot of the SQLite database viewer is included in this repository.

Filename:

```
database.png
```

---

## Technologies Used

- Python
- FastAPI
- SQLite
- sqlite3
- Uvicorn