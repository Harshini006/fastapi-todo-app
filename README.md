# 📝 Daily Task Manager API

**Hey! 👋 Thanks for checking out my first Web API.**

While my main focus as a student is on AI and Machine Learning, my seniors recently gave me some great advice: *knowing how to train an AI model isn't enough if you don't know how to deploy it so people can actually use it.*

I took that advice to heart and built this Daily Task Manager using **FastAPI**! This project was my hands-on crash course in backend architecture. I built out the database logic myself to handle full Create, Read, Update, and Delete (CRUD) operations, complete with strict Pydantic data validation. It was an amazing experience connecting the dots between Python code and a live web server, and serves as my foundational step toward eventually deploying full-stack AI applications.

---

## ✨ Features
* **CRUD Operations:** Full Create, Read, Update, and Delete functionality for daily tasks.
* **Bulk Insert:** A custom `/tasks/bulk` endpoint to schedule multiple tasks at once.
* **Data Validation:** Strict type-checking using **Pydantic** models to prevent bad data.
* **Custom Filtering:** Specialized endpoints (e.g., fetching only "pending" tasks).
* **Error Handling:** Custom HTTP exceptions (404, 422, 400) for missing or duplicate data.

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Validation:** Pydantic

## 🚀 How to Run Locally

If you want to download and test this API on your own machine, follow these steps in your terminal:

**1. Clone the repository:**
`git clone https://github.com/Harshini006/fastapi-todo-app.git`
`cd fastapi-todo-app`

**2. Install the required dependencies:**
`pip install fastapi uvicorn`

**3. Start the local server:**
`uvicorn main:app --reload`

**4. Test the API:**
Open your web browser and navigate to the interactive Swagger UI documentation at:
👉 `http://127.0.0.1:8000/docs`

## 📡 API Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tasks/` | Create a new daily task |
| `POST` | `/tasks/bulk` | Add multiple tasks at once |
| `GET`  | `/tasks/` | Retrieve the entire daily schedule |
| `GET`  | `/tasks/pending`| Retrieve only tasks marked as not done |
| `PUT`  | `/tasks/{task_id}` | Update a task's details or completion status |
| `DELETE`| `/tasks/{task_id}` | Remove a task from the schedule |

---
