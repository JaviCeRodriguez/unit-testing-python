import unittest

from entities.product import Product, ProductDiscountError

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        self.smarthphone = Product(self.name, self.price)

    
    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name, 'El nombre del producto no es correcto')
        self.assertEqual(product.price, price, 'El precio del producto no es correcto')
    

    def test_product_name(self):
        self.assertEqual(self.smarthphone.name, self.name, 'El nombre del producto no es correcto')


    def test_product_price(self):
        self.assertEqual(self.smarthphone.price, self.price, 'El precio del producto no es correcto')