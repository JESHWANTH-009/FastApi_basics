from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,conint ,constr ,StringConstraints,Field
from pydantic.functional_validators import field_validator
from typing import Annotated
## compare email pattern,conint used to check only positive, 
##regular expression  regex to username pattern

app=FastAPI()
class User(BaseModel):
    user_name:Annotated[str, StringConstraints(pattern=r'^[A-Za-z0-9_-]+$')]
    age:Annotated[int, Field(gt=0)]
    mail:EmailStr
    #custom validator
    @field_validator('user_name')
    def username_not_spaces(cls,v):
        if ' ' in v:
            raise ValueError('username should not contain spaces')
        return v



@app.post('/register/')
async def register_user(user:User):
    return user

    ## before running install pydantics[email] ---
    ##pip install pydantic[email]