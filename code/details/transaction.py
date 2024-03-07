from details.product import Product
from details.user import User
from details.card import Card

class Transaction:
    uuid: str
    user: User
    product: Product
    card: Card

    def __init__(self, 
                 uuid, 
                 user: User, 
                 product: Product,
                 card: Card):
        
        self.uuid = uuid
        self.user = user
        self.product = product
        self.card = card