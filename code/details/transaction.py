from details.product import Product
from details.user import User
from details.card import Card
import uuid
from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base() #Base class from sqlalchemy

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    user: User = Mapped["User"]
    product: Product = Mapped["Product"]
    card: Card = Mapped["Card"]

    def __init__(self, 
                 uuid, 
                 user: User, 
                 product: Product,
                 card: Card):
        
        self.uuid = uuid
        self.user = user
        self.product = product
        self.card = card