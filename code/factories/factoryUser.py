from details.userDetails import UserDetails
from factories.factory import Factory

class FactoryUser(Factory):
    def __init__(self):
        pass
    
    def create_user(self, user_data=None, **kwargs):
        if user_data is None:
            user_data = kwargs
        else:
            user_data.update(kwargs)

        user = super().create(UserDetails, **user_data)

        return user
