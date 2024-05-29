# SQLAlchemy models

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import uuid

Base = declarative_base()


class Admins(Base):
    __tablename__ = "admins"

    id = Column(String, primary_key=True, default=str(uuid.uuid1()))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Cars(Base):
    __tablename__ = "cars"
    reg_number = Column(String(8), nullable=False, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    parked = Column(Boolean, nullable=False)
    vehicle_type = Column(String, nullable=False)
    time_in = Column(DateTime, nullable=False, default=func.now())
    time_out = Column(DateTime, nullable=False, default=func.now())


engine = create_engine("sqlite:///mydatabase.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
