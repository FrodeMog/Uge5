import sqlite3
from uuid import UUID
from typing import Optional
import json
from factories.factory import Factory

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
        if 'uuid' in annotations:
            fields = ", ".join([f"id INTEGER PRIMARY KEY AUTOINCREMENT"] + [f"{name} {self.get_sqlite_type(value)}" for name, value in annotations.items()])  # Don't add the uuid field
        else:
            fields = ", ".join([f"id INTEGER PRIMARY KEY AUTOINCREMENT", f"uuid TEXT UNIQUE NOT NULL"] + [f"{name} {self.get_sqlite_type(value)}" for name, value in annotations.items()])  # Include the id and uuid fields
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})")
        self.connection.commit()

    def insert_object(self, obj):
        cursor = self.get_cursor()
        table_name = obj.__class__.__name__.lower()
        fields = ", ".join(["uuid"] + list(obj.__class__.__annotations__.keys()))  # Include the uuid field
        placeholders = ", ".join("?" * (len(obj.__class__.__annotations__) + 1))  # Include a placeholder for the uuid
        values = [str(obj.uuid)] + [self.serialize(getattr(obj, name)) for name in obj.__class__.__annotations__.keys()]  # Include the uuid value and serialize objects that can be serialized to JSON
        cursor.execute(f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})", tuple(values))
        self.connection.commit()

    def serialize(self, obj):
        try:
            return json.dumps(obj.__dict__)
        except (TypeError, AttributeError):
            return str(obj)

    def get_object(self, cls):
        cursor = self.get_cursor()
        table_name = cls.__name__.lower()
        cursor.execute(f"SELECT * FROM {table_name}")
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            return {description[0]: value for description, value in zip(cursor.description, row)} # Return a dictionary with the column names as keys

    def get_sqlite_type(self, type_hint):
        if type_hint == str or type_hint == UUID:
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
        elif type_hint == Optional[str] or type_hint == Optional[UUID]:
            return "TEXT"
        elif type_hint == Optional[dict]:
            return "TEXT"
        elif type_hint in Factory().type_map.values():  # Check if the type hint is one of the types in the Factory class
            return "TEXT"  # Store the object as a JSON string
        else:
            raise ValueError(f"Unsupported type hint: {type_hint}")