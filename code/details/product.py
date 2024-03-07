from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base() #Base class from sqlalchemy

class Product(Base):
    __tablename__ = 'products'

    uuid: str = Column(String, primary_key=True)
    manufacturer_id: str = Column(String)
    manufacturer: str = Column(String)
    name: str = Column(String)
    price: float = Column(Float)
    currency: str = Column(String)
    quantity: Optional[int] = Column(Integer)
    weight: Optional[float] = Column(Float)
    color: Optional[str] = Column(String)
    release_year: Optional[int] = Column(Integer)
    description: Optional[str] = Column(String)
    category: Optional[str] = Column(String)
    sub_category: Optional[str] = Column(String)
    rating: Optional[dict] = Column(JSON) 
    technical_specs: Optional[dict] = Column(JSON)

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