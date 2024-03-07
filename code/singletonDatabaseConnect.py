import sqlite3
from typing import Optional

class SingletonDatabaseConnect:
    def __new__(cls, db_url=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonDatabaseConnect, cls).__new__(cls)
            cls.instance.db_url = db_url
            cls.instance.connection = sqlite3.connect(cls.instance.db_url)
        return cls.instance

    def get_session(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor()
    
    def create_table_from_class(self, cls):
        cursor = self.get_cursor()
        table_name = cls.__name__.lower()
        annotations = cls.__annotations__
        if not annotations:
            raise ValueError(f"Class {cls.__name__} doesn't have any annotations")
        fields = ", ".join(f"{name} {self.get_sqlite_type(value)}" for name, value in annotations.items())
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})")
        self.connection.commit()

    def insert_object(self, obj):
        cursor = self.get_cursor()
        table_name = obj.__class__.__name__.lower()
        fields = ", ".join(obj.__class__.__annotations__.keys())
        placeholders = ", ".join("?" * len(obj.__class__.__annotations__))
        values = tuple(getattr(obj, name) for name in obj.__class__.__annotations__.keys())
        cursor.execute(f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})", values)
        self.connection.commit()

    def get_object(self, cls):
        cursor = self.get_cursor()
        table_name = cls.__name__.lower()
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchone()

    def get_sqlite_type(self, type_hint):
        if type_hint == str:
            return "TEXT"
        elif type_hint == int:
            return "INTEGER"
        elif type_hint == float:
            return "REAL"
        elif type_hint == dict:
            return "TEXT"  # Store dicts as JSON strings
        elif type_hint == Optional[int]:
            return "INTEGER"
        elif type_hint == Optional[float]:
            return "REAL"
        elif type_hint == Optional[str]:
            return "TEXT"
        elif type_hint == Optional[dict]:
            return "TEXT"
        else:
            raise ValueError(f"Unsupported type hint: {type_hint}")