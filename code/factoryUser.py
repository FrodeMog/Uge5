from details.userDetails import UserDetails
from details.loginDetails import LoginDetails

class FactoryUser:
    def __init__(self):
        pass

    def create_user(self,
                    user_id,
                    name,
                    age,
                    email,
                    address,
                    shipping_address,
                    phone,
                    loginDetails: LoginDetails):
        
        if not all([user_id, name, age, email, address, shipping_address, phone, loginDetails]):
            raise ValueError("Mandatory fields cannot be empty")

        user = UserDetails(user_id, name, age, email, address, shipping_address, phone, loginDetails)

        return user