#this helps to define structure of task like title ,description

from pydantic import BaseModel

class Task(BaseModel):
    id:int
    title:str
    description:str

class Config:
    from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
