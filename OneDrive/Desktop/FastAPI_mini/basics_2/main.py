from fastapi import FastAPI
from pydantic import BaseModel,field_validator,Field
app=FastAPI()
class User(BaseModel):
    name:str
    age:int =Field(...,gt=0,le=120)
    @field_validator("name")
    def name_not_empty(cls,v):
        if not v:
            raise ValueError("Name must not empty")
        return v

@app.post('/users/')
async def create_user(user:User):
    u={"name":user.name,"age":user.age}
    return u    # if greater 120 given Error unproceesable entity

@app.get('/users/{user_id}',response_model=User)
async def get_user(user_id:int):
    return {"name":"Jeshwanth","age":23}