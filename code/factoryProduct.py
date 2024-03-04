from productDetails import ProductDetails
from userDetails import UserDetails
from transactionDetails import TransactionDetails

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

class FactoryUser:
    def __init__(self):
        pass

    def create_user(self, user_id, name, age, email, address, shipping_address, phone, loginDetails):
        if not all([user_id, name, age, email, address, shipping_address, phone, loginDetails]):
            raise ValueError("Mandatory fields cannot be empty")

        user = UserDetails(user_id, name, age, email, address, shipping_address, phone, loginDetails)

        return user

class FactoryTransaction:
    def __init__(self):
        pass

    def create_transaction(self, transactionId, userDetails, Product, cardDetails):
        if not all([transactionId, userDetails, Product, cardDetails]):
            raise ValueError("Mandatory fields cannot be empty")

        transaction = TransactionDetails(transactionId, userDetails, Product, cardDetails)

        return transaction