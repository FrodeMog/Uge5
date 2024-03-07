import unittest
from factories.factory import Factory
from singletonDatabaseConnect import SingletonDatabaseConnect
from singletonDatabaseConnectSQLAlchemy import SingletonDatabaseConnectSQLAlchemy
from sqlalchemy import inspect
#python -m unittest newTest.py

class TestData(unittest.TestCase):
    def __init__(self):
        loginFactory = Factory("login")
        productFactory = Factory("product")
        userFactory = Factory("user")
        cardFactory = Factory("card")
        self.product_data = {
            "currency": "USD",
            "manufacturer": "Apple",
            "manufacturer_id": "APPLE_123",
            "price": 1000,
            "name": "iPhone",
            "color": "black"
        }
        self.login_data = {
            "username": "user",
            "password": "pass"
        }
        login = loginFactory.create(self.login_data)
        self.user_data = {
            "name": "John",
            "age": 30,
            "email": "john@email.com",
            "address": "123 fake st",
            "shipping_address": "123 fake st",
            "phone": "123456789",
            "login": login,  
        }
        self.card_data = {
            "card_number": "123456789",
            "card_holder_name": "John",
            "expiry_date": "12/23",
            "cvv": "123"
        }
        user = userFactory.create(self.user_data)
        product = productFactory.create(self.product_data)
        card = cardFactory.create(self.card_data)
        self.transaction_data = {
            "user": user,
            "product": product,
            "card": card,
        }

class TestFactory(unittest.TestCase):
    def setUp(self):
        self.test_data = TestData()
        self.product_data = self.test_data.product_data
        self.login_data = self.test_data.login_data
        self.user_data = self.test_data.user_data
        self.card_data = self.test_data.card_data
        self.transaction_data = self.test_data.transaction_data

    def test_create_product(self):
        productFactory = Factory("product")
        product = productFactory.create(self.product_data)
        for key, value in self.product_data.items():
            self.assertEqual(getattr(product, key), value)

    def test_create_product_invalid_price(self):
        productFactory = Factory("product")
        self.product_data["price"] = -100
        with self.assertRaises(ValueError):
            productFactory.create(self.product_data)
    
    def test_create_product_missing_values(self):
        productFactory = Factory("product")
        self.product_data.pop("currency")
        with self.assertRaises(ValueError):
            productFactory.create(self.product_data)
    
    def test_create_login(self):
        loginFactory = Factory("login")
        login = loginFactory.create(self.login_data)
        for key, value in self.login_data.items():
            self.assertEqual(getattr(login, key), value)

    def test_create_login_missing_values(self):
        loginFactory = Factory("login")
        self.login_data.pop("username")
        with self.assertRaises(ValueError):
            loginFactory.create(self.login_data)
    
    def test_create_user(self):
        userFactory = Factory("user")
        user = userFactory.create(self.user_data)
        for key, value in self.user_data.items():
            if key == "login":
                self.assertEqual(type(getattr(user, key)), value.__class__)
            else:
                self.assertEqual(getattr(user, key), value)
    
    def test_create_user_missing_values(self):
        userFactory = Factory("user")
        self.user_data.pop("name")
        with self.assertRaises(ValueError):
            userFactory.create(self.user_data)
    
    def test_create_card(self):
        cardFactory = Factory("card")
        card = cardFactory.create(self.card_data)
        for key, value in self.card_data.items():
            self.assertEqual(getattr(card, key), value)
    
    def test_create_card_missing_values(self):
        cardFactory = Factory("card")
        self.card_data.pop("card_number")
        with self.assertRaises(ValueError):
            cardFactory.create(self.card_data)

    def test_create_transaction(self):
        transactionFactory = Factory("transaction")
        transaction = transactionFactory.create(self.transaction_data)
        for key, value in self.transaction_data.items():
            self.assertEqual(getattr(transaction, key), value)
    
    def test_create_transaction_missing_values(self):
        transactionFactory = Factory("transaction")
        self.transaction_data.pop("user")
        with self.assertRaises(ValueError):
            transactionFactory.create(self.transaction_data)

    def test_create_multiple_products(self):
        productFactory = Factory("product")
        products = []
        for _ in range(10):
            product_data = self.product_data.copy()
            product_data.pop("uuid", None)  # Remove the uuid if it exists
            product = productFactory.create(product_data)
            products.append(product)
        
        for i in range(10):
            self.assertNotEqual(products[i].uuid, products[i-1].uuid)

class TestSingletonDatabaseConnect(unittest.TestCase):
    def setUp(self):
        self.db_url = ":memory:"
        self.db = SingletonDatabaseConnect(self.db_url)
        self.test_data = TestData()
        self.product_data = self.test_data.product_data
        self.login_data = self.test_data.login_data
        self.user_data = self.test_data.user_data
        self.card_data = self.test_data.card_data
        self.transaction_data = self.test_data.transaction_data
    
    def test_singleton(self):
        db = SingletonDatabaseConnect(self.db_url)
        self.assertEqual(self.db, db)

    def test_get_cursor(self):
        cursor = self.db.get_cursor()
        self.assertIsNotNone(cursor)
    
    def test_get_session(self):
        session = self.db.get_session()
        self.assertIsNotNone(session)

    def test_connection_is_singleton(self):
        db1 = SingletonDatabaseConnect(self.db_url)
        db2 = SingletonDatabaseConnect(self.db_url)
        connection1 = db1.connection
        connection2 = db2.connection
        self.assertIs(connection1, connection2)
    
    def test_factory_product(self):
        factory = Factory("product")
        product = factory.create(self.product_data)

        self.db.create_table_from_class(type(product))
        
        self.db.insert_object(product)

        result = self.db.get_object(type(product), uuid = product.uuid)
        self.assertEqual(result["uuid"], str(product.uuid))
    
    def test_factory_login(self):
        factory = Factory("login")
        login = factory.create(self.login_data)

        self.db.create_table_from_class(type(login))
        
        self.db.insert_object(login)

        result = self.db.get_object(type(login), username = login.username)
        self.assertEqual(result["username"], str(login.username))

    def test_factory_user(self):
        factory = Factory("user")
        user = factory.create(self.user_data)

        self.db.create_table_from_class(type(user))
        
        self.db.insert_object(user)

        result = self.db.get_object(type(user), uuid = user.uuid)
        self.assertEqual(result["uuid"], str(user.uuid))
    
    def test_factory_card(self):
        factory = Factory("card")
        card = factory.create(self.card_data)

        self.db.create_table_from_class(type(card))
        
        self.db.insert_object(card)

        result = self.db.get_object(type(card), card_number = card.card_number)
        self.assertEqual(result["card_number"], str(card.card_number))

    def test_factory_transaction(self):
        factory = Factory("transaction")
        transaction = factory.create(self.transaction_data)

        self.db.create_table_from_class(type(transaction))
        
        self.db.insert_object(transaction)

        result = self.db.get_object(type(transaction), uuid = transaction.uuid)
        self.assertEqual(result["uuid"], str(transaction.uuid))
    
    def test_create_multiple_products(self):
        factory = Factory("product")
        product = factory.create(self.product_data)
        self.db.create_table_from_class(type(product))
        
        for _ in range(10):
            # Create a new product and store it in the database
            product_data = self.product_data.copy()
            product_data.pop("uuid", None)  # Ensure a new UUID is generated
            product = factory.create(product_data)
            self.db.insert_object(product)

        # Retrieve all products from the database
        results = list(self.db.get_all_objects(type(product)))

        # Check that all products have a unique id and uuid
        ids = [result["id"] for result in results]
        uuids = [result["uuid"] for result in results]
        self.assertEqual(len(ids), len(set(ids)), "IDs are not unique")
        self.assertEqual(len(uuids), len(set(uuids)), "UUIDs are not unique")
        
class TestSingletonDatabaseConnectSQLAlchemy(unittest.TestCase):
    def setUp(self):
        self.db_url = "sqlite:///:memory:"
        self.db = SingletonDatabaseConnectSQLAlchemy(self.db_url)
        self.test_data = TestData()
        self.product_data = self.test_data.product_data
        self.login_data = self.test_data.login_data
        self.user_data = self.test_data.user_data
        self.card_data = self.test_data.card_data
        self.transaction_data = self.test_data.transaction_data
    
    def test_singleton(self):
        db = SingletonDatabaseConnectSQLAlchemy(self.db_url)
        self.assertEqual(self.db, db)
    
    def test_get_session(self):
        session = self.db.get_session()
        self.assertIsNotNone(session)
    
    def test_engine_is_singleton(self):
        db1 = SingletonDatabaseConnectSQLAlchemy(self.db_url)
        db2 = SingletonDatabaseConnectSQLAlchemy(self.db_url)
        engine1 = db1.get_engine()
        engine2 = db2.get_engine()
        self.assertIs(engine1, engine2)

    def test_factory_product(self):
        factory = Factory("product")
        product = factory.create(self.product_data)

        session = self.db.get_session()
        engine = self.db.get_engine()

        type(product).metadata.create_all(engine) # Create table

        session.add(product)
        session.commit()

        result = session.query(type(product)).filter_by(uuid=product.uuid).first()
        self.assertEqual(result.uuid, product.uuid)

    def test_factory_login(self):
        factory = Factory("login")
        login = factory.create(self.login_data)

        session = self.db.get_session()
        engine = self.db.get_engine()

        type(login).metadata.create_all(engine)

        session.add(login)
        session.commit()

        result = session.query(type(login)).filter_by(uuid=login.uuid).first()
        self.assertEqual(result.uuid, login.uuid)
    
    def test_factory_user(self):
        factory = Factory("user")
        user = factory.create(self.user_data)

        session = self.db.get_session()
        engine = self.db.get_engine()

        type(user).metadata.create_all(engine)

        session.add(user)
        session.commit()

        result = session.query(type(user)).filter_by(uuid=user.uuid).first()
        self.assertEqual(result.uuid, user.uuid)
    
    def test_factory_card(self):
        factory = Factory("card")
        card = factory.create(self.card_data)

        session = self.db.get_session()
        engine = self.db.get_engine()

        type(card).metadata.create_all(engine)

        session.add(card)
        session.commit()

        result = session.query(type(card)).filter_by(uuid=card.uuid).first()
        self.assertEqual(result.uuid, card.uuid)
    
    def test_factory_transaction(self):
        factory = Factory("transaction")
        transaction = factory.create(self.transaction_data)

        session = self.db.get_session()
        engine = self.db.get_engine()

        type(transaction).metadata.create_all(engine)

        session.add(transaction)
        session.commit()

        result = session.query(type(transaction)).filter_by(uuid=transaction.uuid).first()
        self.assertEqual(result.uuid, transaction.uuid)

class CustomTestResult(unittest.TextTestResult):
    def printErrors(self):
        self.stream.writeln("Passed: {}".format(self.testsRun - len(self.failures) - len(self.errors)))
        self.stream.writeln("Failed: {}".format(len(self.failures)))
        self.stream.writeln("Errors: {}".format(len(self.errors)))
        super().printErrors()

class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())