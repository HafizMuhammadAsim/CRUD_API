# Task API

A simple RESTful CRUD API built with **FastAPI** for the Week 2 Backend AI Engineering assignment.

This project demonstrates the four basic CRUD operations using an **in-memory list** (no database). The API includes input validation, proper HTTP status codes, and interactive API documentation with Swagger UI.

---

# Features

- Create a task
- Read all tasks
- Read a single task by ID
- Update a task
- Delete a task
- Health check endpoint
- Input validation
- Proper HTTP status codes
- Interactive Swagger UI

---

# Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Pydantic

---

# Installation

Clone the repository:

```bash
git clone https://github.com/HafizMuhammadAsim/CRUD_API.git
```

Go into the project folder:

```bash
cd CRUD_API
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run the Project

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get All Tasks |
| GET | /tasks/{id} | Get Task by ID |
| POST | /tasks | Create New Task |
| PUT | /tasks/{id} | Update Task |
| DELETE | /tasks/{id} | Delete Task |

---

# Example Request

Create a task:

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\":\"Buy Milk\"}"
```

Example Response

```json
HTTP/1.1 201 Created

{
  "id": 4,
  "title": "Buy Milk",
  "done": false
}
```

---

# HTTP Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 | Success |
| 201 | Task Created |
| 204 | Task Deleted |
| 400 | Invalid Request |
| 404 | Task Not Found |

---

# Swagger UI

Open the following URL after running the server:

```
http://127.0.0.1:8000/docs
```

Add a screenshot of the Swagger page below.

![Swagger UI]
<img width="925" height="440" alt="image" src="https://github.com/user-attachments/assets/90b9235d-e561-483b-84cb-99781385aaa0" />


---

# Project Structure

```
CRUD_API/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── swagger.png
└── venv/
```

---

# Assignment Requirements Covered

- ✔ FastAPI Server
- ✔ CRUD Operations
- ✔ In-memory Data Storage
- ✔ Input Validation
- ✔ Correct HTTP Status Codes
- ✔ Swagger UI
- ✔ Public GitHub Repository
- ✔ README Documentation

---

# Author

**HAFIZ MUHAMMAD ASIM**

Backend AI Engineering Internship – Week 2 Assignment
