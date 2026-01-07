from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from .config import settings

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:mypass@localhost/mydb'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
print("DB URL:", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn =psycopg2.connect(host='localhost',database='mydb',user='postgres',password='mypass', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connected successfully!")
#         break
#     except Exception as error:
#         print("Connectin to database failed")
#         print("Error:", error)
#         time.sleep(2)

