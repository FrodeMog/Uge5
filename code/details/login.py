import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Login(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    username: str = Column(String)
    password: str = Column(String)

    def __init__(self, 
                 username, 
                 password):
        
        self.username = username
        self.password = password