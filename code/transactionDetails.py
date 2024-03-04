import productDetails as productDetails
import userDetails as userDetails
import cardDetails as cardDetails

class TransactionDetails:
    def __init__(self, 
                 transactionId, 
                 userDetails: userDetails.UserDetails, 
                 Product: productDetails.ProductDetails,
                 cardDetails: cardDetails.CardDetails):
        
        self.userDetails = userDetails
        self.transactionId = transactionId
        self.Product = Product
        self.cardDetails = cardDetails