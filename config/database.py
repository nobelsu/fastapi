from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///./insurance.db"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
