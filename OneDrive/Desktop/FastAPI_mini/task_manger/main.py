from fastapi import FastAPI
from routers import tasks  ## here routers module helps too import functions from tasks file

app=FastAPI()
app.include_router(tasks.router)  ## including router files
