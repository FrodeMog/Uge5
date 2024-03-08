import uuid
from items.product import Product
from items.user import User
from items.card import Card
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, declarative_base

Base = declarative_base() #Base class from sqlalchemy

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    user = Mapped["User"]
    product = Mapped["Product"]
    card = Mapped["Card"]

    def __init__(self, 
                 uuid, 
                 user: User, 
                 product: Product,
                 card: Card):
        
        self.uuid = uuid
        self.user = user
        self.product = product
        self.card = card