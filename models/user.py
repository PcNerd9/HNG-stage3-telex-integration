from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column
from uuid import uuid4
from db.datbase import session


Base = declarative_base()

class User(Base):

    __tablename__ = "users"

    id = Column(String(64), nullable=False, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(256), nullable=False)


    def new(self, session=session):
        session.add(self)
        session.commit()

    def save(self, session=session):
        session.commit() 

        


    
