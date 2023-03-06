from typing import Union
from fastapi import FastAPI
from database import engine, Base, ToDo
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)
import shemas

app = FastAPI()

@app.get("/")
def read_root():
    return "TODO app"

@app.post("/add")
def add_todo(todo: shemas.ToDo):
    """
        API call for adding a TODO item
    """
    session = Session(bind=engine, expire_on_commit= False)
    todoDB = ToDo(task = todo.task)
    session.add(todoDB)
    session.commit()
    id = todoDB.id
    session.close()
    return f"Created new TODO item with id {id}"

@app.delete("/delete/{id}")
def delete_todo(id: int):
    return "Delete TODO"

@app.put("/update/{id}")
def update_todo():
    return "Update TODO"

@app.get("/get/{id}")
def get_todo():
    return "get TODO"

@app.get("/list")
def get_all_todos():
    return "All TODOs"