from details.loginDetails import LoginDetails

class UserDetails:
    def __init__(self,
                uuid,
                name,
                age,
                email,
                address,
                shipping_address,
                phone,
                loginDetails: LoginDetails):
        
        self.uuid = uuid
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.shipping_address = shipping_address
        self.phone = phone
        self.loginDetails = loginDetails