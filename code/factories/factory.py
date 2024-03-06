import uuid
import inspect
from details.productDetails import ProductDetails as Product
from details.transactionDetails import TransactionDetails as Transaction
from details.userDetails import UserDetails as User
from details.cardDetails import CardDetails as Card
from details.loginDetails import LoginDetails as Login

class Factory:
    def __init__(self, item_type=None):
        self.item_type = item_type
        self.type_map = {
            "product": Product,
            "transaction": Transaction,
            "user": User,
            "login": Login,
            "card": Card,
        }

    def create(self, data_dict=None, **kwargs):
        cls = self.type_map.get(self.item_type)
        if cls is None:
            raise ValueError(f"Invalid item type: {self.item_type}")

        if data_dict is None and not kwargs:
            raise ValueError("No arguments provided")
        
        if data_dict is None:
            data_dict = kwargs
        else:
            data_dict.update(kwargs)

        mandatory_fields = self.get_mandatory_fields(cls)

        # If "uuid" is a mandatory field and its not provided, generate a UUID
        if "uuid" in mandatory_fields and "uuid" not in data_dict:
            data_dict["uuid"] = self.handle_id()

        self.check_mandatory_fields(data_dict, mandatory_fields)

        item = cls(**data_dict)

        return item

    def get_mandatory_fields(self, cls):
        sig = inspect.signature(cls.__init__)
        return [name for name, param in sig.parameters.items() if param.default == inspect.Parameter.empty and name != 'self']

    def check_mandatory_fields(self, product_dict, fields_to_check):
        missing_fields = [field for field in fields_to_check if product_dict.get(field) is None]
        if missing_fields:
            raise ValueError(f"Mandatory fields cannot be empty: {', '.join(missing_fields)}")

    def handle_id(self):
        return str(uuid.uuid4()) # maybe handle differently with a database