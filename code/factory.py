import uuid
import inspect

class Factory:
    def __init__(self):
        pass

    def get_mandatory_fields(self, cls):
        sig = inspect.signature(cls.__init__)
        return [name for name, param in sig.parameters.items() if param.default == inspect.Parameter.empty and name != 'self']

    def check_mandatory_fields(self, product_dict, fields_to_check):
        missing_fields = [field for field in fields_to_check if product_dict.get(field) is None]
        if missing_fields:
            raise ValueError(f"Mandatory fields cannot be empty: {', '.join(missing_fields)}")

    def handle_id(self, id):
        if id is None:
            id = str(uuid.uuid4())  # maybe handle differently with a database
        id = str(id)
        return id