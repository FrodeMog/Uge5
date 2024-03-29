from details.transaction import Transaction
from factories.factory import Factory

class FactoryTransaction(Factory):
    def __init__(self):
        pass
    
    def create_transaction(self, transaction_data=None, **kwargs):
        if transaction_data is None:
            transaction_data = kwargs
        else:
            transaction_data.update(kwargs)

        transaction = super().create(Transaction, **transaction_data)

        return transaction