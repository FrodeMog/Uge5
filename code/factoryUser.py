from typing import Optional
from details.userDetails import UserDetails
from details.loginDetails import LoginDetails
from factory import Factory

class FactoryUser(Factory):
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
        
        user_id = self.handle_id(user_id)
        user =  UserDetails(user_id, name, age, email, address, shipping_address, phone, loginDetails)

        #Error checks
        self.check_mandatory_fields(user.__dict__, self.get_mandatory_fields(UserDetails))

        return user
    
