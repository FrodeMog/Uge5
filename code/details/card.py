import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    card_number: str = Column(String)
    card_holder_name: str = Column(String)
    expiry_date: str = Column(String)
    cvv: str = Column(String)

    def __init__(self, 
                 card_number, 
                 card_holder_name, 
                 expiry_date, 
                 cvv):
        
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.cvv = cvv