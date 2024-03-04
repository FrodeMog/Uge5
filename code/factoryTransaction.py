import uuid
from typing import Optional
from details.transactionDetails import TransactionDetails
from details.productDetails import ProductDetails
from details.userDetails import UserDetails
from details.cardDetails import CardDetails

class FactoryTransaction:
    def __init__(self):
        pass

    def create_transaction(self,
                           userDetails: UserDetails,
                           productDetails: ProductDetails,
                           cardDetails: CardDetails,
                           transaction_id: Optional[str] = None):
        
        if not all([userDetails, productDetails, cardDetails]):
            raise ValueError("Mandatory fields cannot be empty")
        
        transaction_id = self.give_transaction_id(transaction_id)

        transaction = TransactionDetails(transaction_id, userDetails, productDetails, cardDetails)

        return transaction
    
    def give_transaction_id(self, transaction_id):
        if transaction_id is None:
            transaction_id = str(uuid.uuid4()) #maybe handle differently with a database
            return transaction_id