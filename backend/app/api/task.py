from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.db.session import get_db
from app.crud import task as crud_task

router = APIRouter()

@router.get("/tasks", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud_task.get_tasks(db)

@router.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud_task.create_task(db, task)

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return crud_task.update_task(db, task_id, task)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud_task.delete_task(db, task_id)
    return {"ok": True}
