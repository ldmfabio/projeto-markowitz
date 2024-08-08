from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = config('postgresql://postgres:postgres@localhost:5432/db-projeto-markovitz')

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)