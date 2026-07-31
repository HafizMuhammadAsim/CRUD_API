import sqlite3
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    version="1.0"
)

# -------------------------------
# SQLite Database
# -------------------------------

connection = sqlite3.connect("tasks.db", check_same_thread=False)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
)
""")

connection.commit()

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]

if count == 0:
    sample_tasks = [
        ("Learn FastAPI", 0),
        ("Complete CRUD Assignment", 0),
        ("Push Project to GitHub", 1)
    ]

    cursor.executemany(
        "INSERT INTO tasks(title, done) VALUES (?, ?)",
        sample_tasks
    )

    connection.commit()


# -------------------------------
# Request Model
# -------------------------------

class Task(BaseModel):
    title: str | None = None
    done: bool = False


# -------------------------------
# Root Endpoint
# -------------------------------

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }


# -------------------------------
# Health Check
# -------------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -------------------------------
# Get All Tasks
# -------------------------------

@app.get("/tasks")
def get_tasks():

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "done": bool(row["done"])
        }
        for row in rows
    ]


# -------------------------------
# Get Task By ID
# -------------------------------

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": f"Task {task_id} not found"
            }
        )

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])
    }



# -------------------------------
# Create Task
# -------------------------------

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):

    if task.title is None or task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Title is required"
            }
        )

    cursor.execute(
        "INSERT INTO tasks(title, done) VALUES (?, ?)",
        (task.title, 0)
    )

    connection.commit()

    new_id = cursor.lastrowid

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (new_id,)
    )

    row = cursor.fetchone()

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])
    }

# -------------------------------
# Update Task
# -------------------------------

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    if updated_task.title is None or updated_task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Title is required"
            }
        )

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": f"Task {task_id} not found"
            }
        )

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, done = ?
        WHERE id = ?
        """,
        (updated_task.title, int(updated_task.done), task_id)
    )

    connection.commit()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])
    }


# -------------------------------
# Delete Task
# -------------------------------

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": f"Task {task_id} not found"
            }
        )

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    return