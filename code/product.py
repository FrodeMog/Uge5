from typing import Optional

class Product:
    def __init__(self, 
                product_id: str, 
                manufacturer_id: str, 
                manufacturer: str, 
                name: str, 
                price: float, 
                currency: str, 
                quantity: Optional[int] = None, 
                weight: Optional[float] = None, 
                color: Optional[str] = None, 
                release_year: Optional[int] = None, 
                description: Optional[str] = None, 
                category: Optional[str] = None, 
                sub_category: Optional[str] = None, 
                #image: Optional[#Image object] = None, #Maybe implement later
                rating: Optional[dict] = None, 
                tecnical_specs: Optional[dict] = None):
        self.product_id = product_id            #ID on sales page
        self.manufacturer_id = manufacturer_id  #ID from manufacturer
        self.manufacturer = manufacturer        #Name of the manufacturer
        self.name = name                        #Name of the product
        self.price = price                      #Price of the product
        self.currency = currency                #Currency of the price. EX: USD, EUR, DKK
        self.quantity = quantity                #Quantity of the product
        self.weight = weight                    #Weight of the product in kg
        self.color = color                      #Color of the product
        self.release_year = release_year        #Year of release
        self.description = description          #Description of the product
        self.category = category                #Category of the product. EX: Electronics, Clothing, Food
        self.sub_category = sub_category        #Sub category of the product. EX: Smartphone, T-shirt, Apple
        #self.image = image                     #Image of the product
        self.rating = rating                    #Rating of the product
        self.tecnical_specs = tecnical_specs    #Tecnical specs of the product