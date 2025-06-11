from fastapi import FastAPI,Form,UploadFile,File
from pydantic import BaseModel

app=FastAPI()

@app.post('/login')
async def login(username:str=Form(...),Password:str=Form(...)):
    return {"username":username,"message":"Login Succesfull"}

@app.post('/upload/')
async def upload_file(file:UploadFile=File(...)):
    return {"filename":file.filename}