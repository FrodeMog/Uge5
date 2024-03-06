from typing import Optional
from details.transactionDetails import TransactionDetails
from details.productDetails import ProductDetails
from details.userDetails import UserDetails
from details.cardDetails import CardDetails
from factory import Factory

class FactoryTransaction(Factory):
    def __init__(self):
        pass

    def create_transaction(self,
                           userDetails: UserDetails,
                           productDetails: ProductDetails,
                           cardDetails: CardDetails,
                           transaction_id: Optional[str] = None):
        
        transaction_id = self.handle_id(transaction_id)
        transaction = TransactionDetails(transaction_id, userDetails, productDetails, cardDetails)

        #Error checks
        self.check_mandatory_fields(transaction.__dict__, self.get_mandatory_fields(TransactionDetails))

        return transaction