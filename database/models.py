# SQLAlchemy models

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

from uuid import uuid4

Base = declarative_base()


class Admin(Base):
    __tablename__ = "admins"

    id = Column(String, primary_key=True, default=str(uuid4()))
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Car(Base):
    __tablename__ = "cars"

    id = Column(String, primary_key=True, default=str(uuid4()))
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    user_id = Column(String, ForeignKey("users.id"))
    time = Column(DateTime, nullable=False, default=func.now())
