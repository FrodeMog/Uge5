class Login:
    username: str
    password: str
    #Do some password hashing / encryption here
    def __init__(self,
                 username,
                 password):
        
        self.username = username
        self.password = password