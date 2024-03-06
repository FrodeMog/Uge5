from details.productDetails import ProductDetails
from details.userDetails import UserDetails
from details.cardDetails import CardDetails

class TransactionDetails:
    def __init__(self, 
                 uuid, 
                 userDetails: UserDetails, 
                 productDetails: ProductDetails,
                 cardDetails: CardDetails):
        
        self.uuid = uuid
        self.userDetails = userDetails
        self.productDetails = productDetails
        self.cardDetails = cardDetails