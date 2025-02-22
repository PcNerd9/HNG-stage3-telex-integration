from sqlalchemy import Column, String
from .user import Base
from uuid import uuid4
from db.datbase import session


class Channels(Base):

    __tablename__ = "channels"

    id = Column(String(64), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    channel_url = Column(String(256))

    def save(self, session=session):
        session.add(self)
        session.commit()