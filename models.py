#!flask/bin/python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    website = Column(String(255))

if __name__ == "__main__":
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))
    from sqlalchemy import create_engine
    #from .settings import DB_URI
    print("Ace of Base")
    print(Base.metadata)
    print("creating engine")
    engine = create_engine('sqlite:///.sqlite3')
    print("dropping metadata")
    Base.metadata.drop_all(engine)
    print("creating all models")
    Base.metadata.create_all(engine)
