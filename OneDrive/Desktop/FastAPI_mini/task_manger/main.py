from fastapi import FastAPI
from routers import tasks  ## here routers module helps too import functions from tasks file

app=FastAPI()
app.include_router(tasks.router,prefix='/api')  ## including router files
