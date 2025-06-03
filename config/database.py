from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+asyncmy://root:Shuriken3108@localhost/insurance_db"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL.replace("asyncmy", "pymysql"))
