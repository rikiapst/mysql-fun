from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create an engine
engine = create_engine("mysql://admin:databasetest@database-1.co1vivjyehts.us-east-2.rds.amazonaws.com/testdb12", echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()