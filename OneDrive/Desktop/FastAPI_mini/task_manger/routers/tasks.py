# # thisx is used for curd operations

from fastapi import APIRouter,HTTPException
from schemas import Task  ## calling class Task in schemas.py

router=APIRouter()

task_db=[] ## to store tasks
@router.get('/tasks')  #/taks is url 
def list_tasks(skip:int=0,limit:int=10):
    return task_db[skip:skip+limit]

@router.get('/tasks/{task_id}')## to read task
def get_task(task_id:int):
    for i in task_db:    #here i is 1 seperate task stored in task_db
        if i["id"]==task_id:   #here getting task with id as created in schemas.py
            return i
    raise HTTPException(status_code=404,detail="not found task")

@router.post('/tasks') ## to add  task
def create_task(task:Task):
    task_db.append(task.dict())
    return {"message":"Task created","task":task.dict()}

@router.put('/tasks/{task_id}')
def update_task(task_id:int,updated_task:Task):
    for i,task in enumerate(task_db):  ## enumaaerate used to get values of id and task in a pattern
        if task["id"]==task_id:
            task_db[i]=updated_task.dict()
            return {"message":f"Update tasks {task_id}","task":updated_task.dict()}
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete('/tasks/{task_id}')
def delete_task(task_id:int):
    for i,task in enumerate(task_db):
        if task["id"]==task_id:
            task_db.pop(i)
            return {"meassage":f"Delete task {task_id}"}
    raise HTTPException(status_code=404, detail="Task not found")