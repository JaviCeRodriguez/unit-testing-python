import unittest

from entities.product import Product, ProductDiscountError
from entities.shopping_cart import ShoppingCart


def is_available_to_skip() -> bool:
    return True


def is_connected() -> bool:
    return False


class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        self.smarthphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smarthphone)


    def tearDown(self):
        pass


    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'El carrito de compras no esta vacio')


    def test_shopping_has_product(self):
        self.assertFalse(self.shopping_cart_1.has_products(), 'El carrito de compras tiene productos')
        self.assertTrue(self.shopping_cart_2.has_products(), 'El carrito de compras no tiene productos')


    def test_products_in_shopping_cart(self):
        self.assertIn(self.smarthphone, self.shopping_cart_2.products, 'El producto no esta en el carrito de compras')

        product = Product('Laptop', 1000.00)
        self.shopping_cart_2.add_product(product)

        self.assertIn(product, self.shopping_cart_2.products, 'El producto no esta en el carrito de compras')
    

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smarthphone)
        self.assertNotIn(self.smarthphone, self.shopping_cart_2.products, 'El producto esta en el carrito de compras')


    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Laptop', price=1000.00, discount=2000.00)

    
    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=100.00))
        self.shopping_cart_1.add_product(Product(name='Laptop', price=1000.00, discount=200.00))

        self.assertGreater(self.shopping_cart_1.total, 0, 'El total del carrito de compras no es correcto')
        self.assertLess(self.shopping_cart_1.total, 1000.00, 'El total del carrito de compras no es correcto')
        # assertGreaterEqual
        # assertLessEqual
        self.assertEqual(self.shopping_cart_1.total, 900.00, 'El total del carrito de compras no es correcto')


    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0, 'El total del carrito de compras no es correcto')


    @unittest.skip('Motivo de la prueba que se va a omitir')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    
    # skipIf -> Evalua sobre verdadero
    # skipUnlesse -> Evalua sobre falso
    @unittest.skipIf(is_available_to_skip(), 'No se ejecuta la prueba')
    def test_skip_if_example(self):
        self.assertEqual(1, 1)
    

    @unittest.skipUnless(is_connected(), 'No se ejecuta la prueba')
    def test_skip_unless_example(self):
        self.assertEqual(1, 1)


    def test_code_product(self):
        self.assertRegex(self.smarthphone.code, r'^code-.*$', 'El codigo del producto no es correcto')


if __name__ == '__main__':
    unittest.main()