# SQLAlchemy models

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import uuid

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=str(uuid.uuid1()))
    role = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Car(Base):
    __tablename__ = "cars"

    id = Column(String, primary_key=True, default=str(uuid.uuid1()))
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    user_id = Column(String, ForeignKey("users.id"))
    time = Column(DateTime, nullable=False, default=func.now())


engine = create_engine("sqlite:///mydatabase.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
# Insert sample users
user1 = Users(role="admin", email="percymagoras@gmail.com", password="percy2004")

session.add(user1)
session.commit()

# Insert sample cars
car1 = Car(make="Toyota", model="Corolla", year=2015, user_id=user1.id)

session.add(car1)
session.commit()