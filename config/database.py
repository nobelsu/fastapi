from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+aiomysql://root:Shuriken3108@localhost/insurance_db"
SYNC_DATABASE_URL = "mysql+pymysql://root:Shuriken3108@localhost/insurance_db"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(SYNC_DATABASE_URL)
