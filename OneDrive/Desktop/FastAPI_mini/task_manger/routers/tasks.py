# # thisx is used for curd operations

from fastapi import APIRouter


router=APIRouter()

@router.get('/tasks')  #/taks is url 
def list_tasks(skip:int=0,limit:int=10):
    return {"message":f"List tasks from{skip} to {limit}"}

@router.get('/tasks/{task_id}')
def get_task(task_id:int):
    return {"message":f"Get task {task_id}" }
@router.post('/tasks')
def create_task(task_id:int):
    return {"message":"Create a new task"}

@router.put('/tasks/{task_id}')
def update_task(task_id:int):
    return {"message":f"Update tasks {task_id}"}

@router.delete('/tasks/{task_id}')
def delete_task(task_id:int):
    return {"meassage":f"Delete task {task_id}"}