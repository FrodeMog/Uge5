from productDetails import ProductDetails

class FactoryProduct:
    def __init__(self):
        pass

    def create_product(self, product_id, manufacturer_id, manufacturer, name, price, currency, **kwargs):
        if not all([product_id, manufacturer_id, manufacturer, name, price, currency]):
            raise ValueError("Mandatory fields cannot be empty")

        if price <= 0:
            raise ValueError("Price must be a positive number")
        
        product = ProductDetails(product_id, manufacturer_id, manufacturer, name, price, currency, **kwargs)

        return product