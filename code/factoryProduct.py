import uuid
from typing import Optional
from details.productDetails import ProductDetails

class FactoryProduct:
    def __init__(self):
        pass

    def create_product(self,
                       manufacturer_id,
                       manufacturer,
                       name,
                       price,
                       currency,
                       product_id: Optional[str] = None,
                       **kwargs):
        if not all([product_id, manufacturer_id, manufacturer, name, price, currency]):
            raise ValueError("Mandatory fields cannot be empty")

        if price <= 0:
            raise ValueError("Price must be a positive number")
        
        product_id = self.give_product_id(product_id)
        
        product = ProductDetails(product_id, manufacturer_id, manufacturer, name, price, currency, **kwargs)

        return product
    
    def give_product_id(self):
        if give_product_id is None:
            give_product_id = str(uuid.uuid4()) #maybe handle differently with a database
            return give_product_id