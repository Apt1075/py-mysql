from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB_URL = "mysql+pymysql://username:password@localhost:3306/dbname"
DB_URL = "mysql+pymysql://root@localhost:3306/py-mysql"


create_engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=create_engine)

Base = declarative_base()