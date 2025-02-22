from sqlalchemy import String, Column
from uuid import uuid4
from  .user import Base
from db.datbase import session


class FailedLogginAttempt(Base):

    __tablename__ = "failed_login_attempts"

    id = Column(String(64), nullable=False, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String(64), nullable=False)
    ip_address = Column(String(64), nullable=False)
    attempt_time = Column(String(64), nullable=False)

    def new(self, session=session):
        session.add(self)
        session.commit()