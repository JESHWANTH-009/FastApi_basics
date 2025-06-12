#this helps to define structure of task like title ,description

from pydantic import BaseModel

class Task(BaseModel):
    id:int
    title:str
    description:str

class Config:
    orm_mode=True