from typing import Optional
from details.productDetails import ProductDetails
from factory import Factory

class FactoryProduct(Factory):
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
        
        product_id = self.handle_id(product_id)
        product = ProductDetails(product_id, manufacturer_id, manufacturer, name, price, currency, **kwargs)

        #Error checks
        self.check_mandatory_fields(product.__dict__, self.get_mandatory_fields(ProductDetails))

        if price <= 0:
            raise ValueError("Price must be a positive number")
        
        return product