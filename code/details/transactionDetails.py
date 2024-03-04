from productDetails import ProductDetails
from userDetails import UserDetails
from cardDetails import CardDetails

class TransactionDetails:
    def __init__(self, 
                 transactionId, 
                 userDetails: UserDetails, 
                 Product: ProductDetails,
                 cardDetails: CardDetails):
        
        self.userDetails = userDetails
        self.transactionId = transactionId
        self.Product = Product
        self.cardDetails = cardDetails