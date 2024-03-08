import uuid
from items.login import Login
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, declarative_base

Base = declarative_base() #Base class from sqlalchemy

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    name: str = Column(String)
    age: int = Column(Integer)
    email: str = Column(String)
    address: str = Column(String)
    shipping_address: str = Column(String)
    phone: str = Column(String)
    login: Login = Mapped["Login"]   

    def __init__(self,
                uuid,
                name,
                age,
                email,
                address,
                shipping_address,
                phone,
                login: Login):
        
        self.uuid = uuid
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.shipping_address = shipping_address
        self.phone = phone
        self.login = login