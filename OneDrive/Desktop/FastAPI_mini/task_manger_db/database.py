## this almost the same code when excuting sqllite 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db" ## url od sqlite

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) ## this for auto comit changes in db
Base = declarative_base() #this class is used to define orm model and inherit from Base to create table class
