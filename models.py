#!flask/bin/python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FrameSize(Base):
    __tablename__ = 'framesizes'
    # 'Large'
    id = Column(String(10, primary_key=True))

class WheelSize(Base):
    __tablename__ = 'wheelsizes'
    # 'Large'
    id = Column(String(10, primary_key=True))

class Year(Base):
    __tablename__ = 'years'
    # Use the 4 digit year
    id = Column(Integer, primary_key=True)

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    website = Column(String(255))

    def __repr__(self):
        return "<Brand(name='%s')>" % (self.name)

class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brands.id')
    year = Column(Integer, ForeignKey('years.id'))
    name = Column(String(255))

    def __repr__(self):
        return "<Model(name='%s')>" % (self.name)

class Geometry(Base):
    __tablename__ = 'geometry'
    id = Column(Integer, primary_key=True)
    # Foreign Keys
    model_id = Column(Integer, ForeignKey('models.id')
    framesize = Column(String(10), ForeignKey('framesizes.id')
    wheelsize = Column(String(10), ForeignKey('wheelsizes.id')
        
    # Actual Geo (use mm)
    seattube_length = Column(Integer)
    toptube_length = Column(Integer)
    reach = Column(Integer)
    stack = Column(Integer)
    standover = Column(Integer)
    headtube_angle = Column(Integer)
    headtube_length = Column(Integer)
    seattube_angle = Column(Integer)
    chainstay_length = Column(Integer)
    bb_drop = Column(Integer)
    bb_height = Column(Integer)
    wheelbase = Column(Integer)
    front_center = Column(Integer)
    fork_length = Column(Integer)
    fork_offset = Column(Integer)

    def __repr__(self):
        return "<Geometry(name='%s')>" % (self.name)


if __name__ == "__main__":
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))
    from sqlalchemy import create_engine
    #from .settings import DB_URI
    engine = create_engine('sqlite:///.sqlite3')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
