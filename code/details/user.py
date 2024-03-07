from details.login import Login

class User:
    uuid: str
    name: str
    age: int
    email: str
    address: str
    shipping_address: str
    phone: str
    login: Login

    def __init__(self,
                uuid,
                name,
                age,
                email,
                address,
                shipping_address,
                phone,
                login: Login):
        
        self.uuid = uuid
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.shipping_address = shipping_address
        self.phone = phone
        self.login = Login