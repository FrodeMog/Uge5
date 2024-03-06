import unittest
from factoryProduct import FactoryProduct
#python -m unittest tests.py

class TestFactoryProduct (unittest.TestCase):
    def test_create_product(self):
        factory = FactoryProduct()
        product = factory.create_product("1", "Apple", "iPhone", 1000, "USD")
        self.assertEqual(product.manufacturer, "Apple")
        self.assertEqual(product.name, "iPhone")
        self.assertEqual(product.price, 1000)
        self.assertEqual(product.currency, "USD")
        #Check if the product_id is not None
        self.assertIsNotNone(product.product_id)
    
    def test_create_product_with_id(self):
        factory = FactoryProduct()
        product = factory.create_product("1", "Apple", "iPhone", 1000, "USD", "1")
        self.assertEqual(product.product_id, "1")
    
    def test_create_product_with_kwargs(self):
        factory = FactoryProduct()
        product = factory.create_product("1", "Apple", "iPhone", 1000, "USD", "1", color="black")
        self.assertEqual(product.color, "black")

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