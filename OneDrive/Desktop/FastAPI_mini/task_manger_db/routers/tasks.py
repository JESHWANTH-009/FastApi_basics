# # thisx is used for curd operations

from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from schemas import Task as TaskSchema  ## calling class Task in schemas.py

from models import Task as  TaskModel
from database import SessionLocal,engine  #import defined in database.py
from typing import List
TaskModel.metadata.create_all(bind=engine)
router=APIRouter()

#task_db=[] ## to store tasks
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# using database
@router.post('/tasks',response_model=TaskSchema)
def create_task(task:TaskSchema,db:Session=Depends(get_db)):
     ##TaskScema takes input data while depends injects session
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get('/tasks',response_model=List[TaskSchema])  #/taks is url 
def list_tasks(skip:int=0,limit:int=10, db: Session = Depends(get_db)):
    #  return task_db[skip:skip+limit]
    return db.query(TaskModel).offset(skip).limit(limit).all()

@router.get('/tasks/{task_id}',response_model=TaskSchema)## to read task
def get_task(task_id:int,db:Session=Depends(get_db)):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

    """for i in task_db:    #here i is 1 seperate task stored in task_db
        if i["id"]==task_id:   #here getting task with id as created in schemas.py
            return i
    raise HTTPException(status_code=404,detail="not found task")"""


@router.put('/tasks/{task_id}',response_model=TaskSchema)
def update_task(task_id:int,updated_task:TaskSchema,db:Session=Depends(get_db)):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    db.commit()
    db.refresh(task)
    return task    

    """for i,task in enumerate(task_db):  ## enumaaerate used to get values of id and task in a pattern
        if task["id"]==task_id:
            task_db[i]=updated_task.dict()
            return {"message":f"Update tasks {task_id}","task":updated_task.dict()}
    raise HTTPException(status_code=404, detail="Task not found")"""

@router.delete('/tasks/{task_id}')
def delete_task(task_id:int,db:Session=Depends(get_db)):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": f"Task {task_id} deleted"}

    """for i,task in enumerate(task_db):
        if task["id"]==task_id:
            task_db.pop(i)
            return {"meassage":f"Delete task {task_id}"}
    raise HTTPException(status_code=404, detail="Task not found")"""

