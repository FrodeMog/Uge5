from details.productDetails import ProductDetails
from factories.factory import Factory

class FactoryProduct(Factory):
    def __init__(self):
        pass

    def create_product(self, product_data=None, **kwargs):
        if product_data is None:
            product_data = kwargs
        else:
            product_data.update(kwargs)

        product = super().create(ProductDetails, **product_data)

        return product