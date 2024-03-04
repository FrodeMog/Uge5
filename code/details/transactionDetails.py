from productDetails import ProductDetails
from userDetails import UserDetails
from cardDetails import CardDetails

class TransactionDetails:
    def __init__(self, 
                 transaction_id, 
                 userDetails: UserDetails, 
                 productDetails: ProductDetails,
                 cardDetails: CardDetails):
        
        self.transaction_id = transaction_id
        self.userDetails = userDetails
        self.productetails = productDetails
        self.cardDetails = cardDetails