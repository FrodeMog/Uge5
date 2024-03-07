from typing import Optional

class ProductDetails:
    uuid: str
    manufacturer_id: str
    manufacturer: str
    name: str
    price: float
    currency: str
    quantity: Optional[int] = None
    weight: Optional[float] = None
    color: Optional[str] = None
    release_year: Optional[int] = None
    description: Optional[str] = None
    category: Optional[str] = None
    sub_category: Optional[str] = None
    #image: Optional[#Image object] = None, #Maybe implement later
    rating: Optional[dict] = None
    tecnical_specs: Optional[dict] = None

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