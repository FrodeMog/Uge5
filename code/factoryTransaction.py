from details.transactionDetails import TransactionDetails
from details.productDetails import ProductDetails
from details.userDetails import UserDetails
from details.cardDetails import CardDetails

class FactoryTransaction:
    def __init__(self):
        pass

    def create_transaction(self,
                           transactionId,
                           userDetails: UserDetails,
                           productDetails: ProductDetails,
                           cardDetails: CardDetails):
        if not all([transactionId, userDetails, productDetails, cardDetails]):
            raise ValueError("Mandatory fields cannot be empty")

        transaction = TransactionDetails(transactionId, userDetails, productDetails, cardDetails)

        return transaction