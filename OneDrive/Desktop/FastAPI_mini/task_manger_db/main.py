from fastapi import FastAPI
from routers import tasks  ## here routers module helps too import functions from tasks file
from routers import auth


app=FastAPI()
app.include_router(tasks.router,prefix="/api")  ## including router files
app.include_router(auth.router,prefix="/api") ##Authenctication 