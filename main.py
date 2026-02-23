from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="My Daily Plan & Reminder API")

class Task(BaseModel):
    id: int
    title: str
    scheduled_time: str
    is_done: bool


task_db = []

@app.post("/tasks/")
def create_task(new_task: Task):
    
    for task in task_db:
        if task.id == new_task.id:
            raise HTTPException(status_code=400, detail="Task ID already exists!")
            
    task_db.append(new_task)
    return {"message": "Plan scheduled successfully!", "task": new_task}

@app.post("/tasks/bulk")
def create_multiple_tasks(new_tasks: List[Task]):
   
    for task in new_tasks:
        task_db.append(task)
        
    return {"message": f"Successfully added {len(new_tasks)} tasks to your schedule!"}


@app.get("/tasks/pending")
def get_undone_tasks():
    
    undone_tasks = [task for task in task_db if task.is_done == False]
    
    if len(undone_tasks) == 0:
        return {"message": "You have finished all your plans for today!"}
        
    return {"pending_count": len(undone_tasks), "reminders": undone_tasks}

@app.get("/tasks/")
def get_all_tasks():
    return {"total_tasks": len(task_db), "schedule": task_db}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(task_db):
        if task.id == task_id:
            task_db[i] = updated_task
            return {"message": "Task updated successfully!", "task": updated_task}
            
    raise HTTPException(status_code=404, detail="Task not found in your schedule.")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(task_db):
        if task.id == task_id:
            del task_db[i]
            return {"message": "Task deleted successfully!"}
            
    raise HTTPException(status_code=404, detail="Task not found in your schedule.")
