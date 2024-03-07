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
        table_name = cls.__tablename__
        annotations = cls.__table__.columns
        if not annotations:
            raise ValueError(f"Class {cls.__name__} doesn't have any columns")
        fields = ", ".join([f"{column.name} {self.get_sqlite_type(column.type)}" for column in annotations])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})")
        self.connection.commit()

    def insert_object(self, obj):
        cursor = self.get_cursor()
        table_name = getattr(obj.__class__, '__tablename__', obj.__class__.__name__.lower() + "s")
        fields = ", ".join([column.name for column in obj.__class__.__table__.columns])
        placeholders = ", ".join("?" * len(fields.split(', ')))
        values = [getattr(obj, name) for name in fields.split(', ')]
        # Convert unsupported types to strings
        values = [str(value) if not isinstance(value, (int, float, str, bytes, type(None))) else value for value in values]
        cursor.execute(f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})", tuple(values))
        self.connection.commit()

    def get_object(self, cls, **kwargs):
        cursor = self.get_cursor()
        table_name = getattr(cls, '__tablename__', cls.__name__.lower() + "s")
        filters = " AND ".join([f"{key} = ?" for key in kwargs.keys()])
        values = tuple(str(value) for value in kwargs.values())
        cursor.execute(f"SELECT * FROM {table_name} WHERE {filters}", values)
        row = cursor.fetchone()
        if row is None:
            raise ValueError(f"No object of type {cls.__name__} found in the database")
        else:
            return {description[0]: value for description, value in zip(cursor.description, row)}  # Return a dictionary with the column names as keys

    def get_sqlite_type(self, type_hint):
        if isinstance(type_hint, str):
            return "TEXT"
        elif isinstance(type_hint, int):
            return "INTEGER"
        elif isinstance(type_hint, float):
            return "REAL"
        elif isinstance(type_hint, dict):
            return "TEXT"  # Store dicts as JSON strings
        elif type_hint in Factory().type_map.values():  # Check if the type hint is one of the types in the Factory class
            return "TEXT"  # Store the object as a JSON string
        else:
            return str(type_hint).upper()