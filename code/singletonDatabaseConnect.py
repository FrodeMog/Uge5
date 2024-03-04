class SingletonDatabaseConnect:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonDatabaseConnect, cls).__new__(cls)
        return cls.instance