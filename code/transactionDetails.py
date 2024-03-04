import product as product
import userDetails as userDetails

class TransactionDetails:
    def __init__(self, 
                 transactionId, 
                 userDetails: userDetails.UserDetails, 
                 Product: product.Product):
        
        self.userDetails = userDetails
        self.transactionId = transactionId
        self.Product = Product