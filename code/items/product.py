import uuid
from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base() #Base class from sqlalchemy

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    manufacturer_id = Column(String)
    manufacturer= Column(String)
    name = Column(String)
    price = Column(Float)
    currency = Column(String)
    quantity = Column(Integer)
    weight = Column(Float)
    color = Column(String)
    release_year = Column(Integer)
    description = Column(String)
    category = Column(String)
    sub_category = Column(String)
    rating = Column(JSON) 
    technical_specs = Column(JSON)

    def __init__(self, 
                uuid,
                manufacturer_id, 
                manufacturer, 
                name, 
                price, 
                currency, 
                quantity = None, 
                weight = None, 
                color = None, 
                release_year = None, 
                description = None, 
                category = None, 
                sub_category = None, 
                #image = None, #Maybe implement later
                rating = None, 
                tecnical_specs = None):
        
        self.uuid = uuid
        self.manufacturer_id = manufacturer_id
        self.manufacturer = manufacturer
        self.name = name
        self.price = price
        self.currency = currency
        self.quantity = quantity
        self.weight = weight
        self.color = color
        self.release_year = release_year
        self.description = description
        self.category = category
        self.sub_category = sub_category
        #self.image = image
        self.rating = rating
        self.tecnical_specs = tecnical_specs