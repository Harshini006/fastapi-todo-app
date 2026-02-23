from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# 1. INITIALIZE THE APP
app = FastAPI(title="My Daily Plan & Reminder API")

# 2. THE BLUEPRINT (Data Validation)
# This forces every task to have these exact four pieces of information.
class Task(BaseModel):
    id: int
    title: str
    scheduled_time: str
    is_done: bool

# 3. OUR FAKE DATABASE
# A simple list to store your daily tasks in memory.
task_db = []

# ==========================================
# CRUD OPERATIONS START HERE
# ==========================================

# 🟢 CREATE: Add a new plan to your schedule
@app.post("/tasks/")
def create_task(new_task: Task):
    # Check if a task with this ID already exists to prevent duplicates
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

# 🔵 READ ALL: Look at your entire schedule for the day
@app.get("/tasks/")
def get_all_tasks():
    return {"total_tasks": len(task_db), "schedule": task_db}

# 🟠 UPDATE: Mark a task as done (or update the time/title)
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    # Loop through our database to find the task with the matching ID
    for i, task in enumerate(task_db):
        if task.id == task_id:
            # Replace the old task with the new updated task
            task_db[i] = updated_task
            return {"message": "Task updated successfully!", "task": updated_task}
            
    # If the loop finishes and doesn't find the ID, throw an error
    raise HTTPException(status_code=404, detail="Task not found in your schedule.")

# 🔴 DELETE: Remove a mistake or a cancelled plan
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(task_db):
        if task.id == task_id:
            # Delete the item at this specific index in the list
            del task_db[i]
            return {"message": "Task deleted successfully!"}
            
    raise HTTPException(status_code=404, detail="Task not found in your schedule.")