from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g # global variable

load_dotenv()

# connect to db using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
  Base.metadata.create_all(engine)

def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()

  return g.db # return session wrapped in global object, instead of creating a new session each time