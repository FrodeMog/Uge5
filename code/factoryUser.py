import uuid
from typing import Optional
from details.userDetails import UserDetails
from details.loginDetails import LoginDetails

class FactoryUser:
    def __init__(self):
        pass

    def create_user(self,
                    name,
                    age,
                    email,
                    address,
                    shipping_address,
                    phone,
                    loginDetails: LoginDetails,
                    user_id: Optional[str] = None):
        
        user_id = self.give_user_id(user_id)
        user_id = str(user_id)

        user = UserDetails(user_id, name, age, email, address, shipping_address, phone, loginDetails)

        if not all([name, age, email, address, shipping_address, phone, loginDetails]):
            raise ValueError("Mandatory fields cannot be empty")

        return user
    
    def give_user_id(self, user_id):
        if user_id is None:
            user_id = str(uuid.uuid4()) #maybe handle differently with a database
        return user_id