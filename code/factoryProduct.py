class FactoryProduct:
    def __init__(self):
        pass

    def create_product(product_id, manufacturer_id, manufacturer, name, price, currency, **kwargs):
        # Check that the mandatory fields are not empty
        if not all([product_id, manufacturer_id, manufacturer, name, price, currency]):
            raise ValueError("Mandatory fields cannot be empty")

        if price <= 0:
            raise ValueError("Price must be a positive number")

        # Create a product dictionary with mandatory fields
        product = {
            'product_id': product_id,
            'manufacturer_id': manufacturer_id,
            'manufacturer': manufacturer,
            'name': name,
            'price': price,
            'currency': currency,
        }

        # Add optional fields to the product dictionary
        for key, value in kwargs.items():
            product[key] = value

        return product