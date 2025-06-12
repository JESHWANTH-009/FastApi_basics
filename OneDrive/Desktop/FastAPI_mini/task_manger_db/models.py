from sqlalchemy import Column,Integer,String
from database import Base  ## getting from file database

class Task(Base):
    __tablename__='tasks'
    ## naming table name as "tasks"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    description=Column(String)