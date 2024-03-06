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
        product_id = self.give_product_id(product_id)

        product = ProductDetails(product_id, manufacturer_id, manufacturer, name, price, currency, **kwargs)

        #Error checks
        if not all([product_id, manufacturer_id, manufacturer, name, price, currency]):
            missing_fields = [field for field, value in {
                'product_id': product_id,
                'manufacturer_id': manufacturer_id,
                'manufacturer': manufacturer,
                'name': name,
                'price': price,
                'currency': currency
            }.items() if not value]
            raise ValueError(f"Mandatory fields cannot be empty: {', '.join(missing_fields)}")

        if price <= 0:
            raise ValueError("Price must be a positive number")
        
        return product
    
    def give_product_id(self, product_id):
        if product_id is None:
            product_id = str(uuid.uuid4()) #maybe handle differently with a database
        return product_id