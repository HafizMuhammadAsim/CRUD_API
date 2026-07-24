from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    version="1.0"
)

# -------------------------------
# In-memory tasks
# -------------------------------

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Complete CRUD Assignment",
        "done": False
    },
    {
        "id": 3,
        "title": "Push Project to GitHub",
        "done": True
    }
]

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
    return tasks


# -------------------------------
# Get Task By ID
# -------------------------------

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail={
            "error": f"Task {task_id} not found"
        }
    )


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

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# -------------------------------
# Update Task
# -------------------------------

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for task in tasks:

        if task["id"] == task_id:

            if updated_task.title is None or updated_task.title.strip() == "":
                raise HTTPException(
                    status_code=400,
                    detail={
                        "error": "Title is required"
                    }
                )

            task["title"] = updated_task.title
            task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail={
            "error": f"Task {task_id} not found"
        }
    )


# -------------------------------
# Delete Task
# -------------------------------

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise HTTPException(
        status_code=404,
        detail={
            "error": f"Task {task_id} not found"
        }
    )