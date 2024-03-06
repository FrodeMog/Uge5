import unittest
from factories.factory import Factory
#python -m unittest newTest.py

class TestFactory(unittest.TestCase):
    def setUp(self):
        loginFactory = Factory("login")
        productFactory = Factory("product")
        userFactory = Factory("user")
        cardFactory = Factory("card")
        self.product_data = {
            "currency": "USD",
            "manufacturer": "Apple",
            "manufacturer_id": "1",
            "price": 1000,
            "name": "iPhone",
            "color": "black"
        }
        self.login_data = {
            "username": "user",
            "password": "pass"
        }
        self.user_data = {
            "name": "John",
            "age": 30,
            "email": "john@email.com",
            "address": "123 fake st",
            "shipping_address": "123 fake st",
            "phone": "123456789",
            "loginDetails": loginFactory.create(self.login_data),
        }
        self.card_data = {
            "card_number": "123456789",
            "card_holder_name": "John",
            "expiry_date": "12/23",
            "cvv": "123"
        }
        self.transaction_data = {
            "userDetails": userFactory.create(self.user_data),
            "productDetails": cardFactory.create(self.card_data),
            "cardDetails": productFactory.create(self.product_data),
        }

    def test_create_product(self):
        productFactory = Factory("product")
        product = productFactory.create(self.product_data)
        for key, value in self.product_data.items():
            self.assertEqual(getattr(product, key), value)
    
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
        self.transaction_data.pop("userDetails")
        with self.assertRaises(ValueError):
            transactionFactory.create(self.transaction_data)


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