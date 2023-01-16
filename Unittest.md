# Unittest

## 1) Assert

```py
# assert

if __name__ == '__main__':
    try:
        assert 12 == 10, '12 no es igual a 10 man' # AssertionError

        """
        if not 12 == 10: # No es un método pythonico, se prefiere el assert
            raise AssertionError('12 no es igual a 10 man')
        """

        print('>>> El programa continua con su ejecución.')

    except AssertionError as error:
        print('>>> Error: ', error)
```

## 2) Assert parte 2

```py
def suma_numeros_positivos(n1: int, n2: int) -> int:
    """Permite sumar 2 numeros enteros positivos

    Args:
        n1 (int)
        n2 (int)

    Returns:
        int
    """

    assert n1 > 0 and n2 > 0, 'Ambos numeros deben ser positivos'

    return n1 + n2


if __name__ == '__main__':
    resultado = suma_numeros_positivos(-10, 20)
    print(resultado)
```

## 3) Unittest

Al igual que con doctest, si usamos el flag -v al ejecutar este script, nos da mas detalles

```py
import unittest

class TestExample(unittest.TestCase):

    def test_suma_numeros(self):
        numero1 = 10
        numero2 = 20

        resultado = numero1 + numero2
        self.assertEqual(resultado, 30)

    def test_resta_numeros(self):
        numero1 = 20
        numero2 = 20

        resultado = numero1 - numero2
        self.assertEqual(resultado, -10)


if __name__ == '__main__':
    unittest.main()
```

## 4) Estructura del proyecto

Ver carpeta Unittest

```py
# Unittest/test_shopping_cart.py

import unittest

from product import Product


class TestShoppingCart(unittest.TestCase):

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name, 'El nombre del producto no es correcto')
        self.assertEqual(product.price, price, 'El precio del producto no es correcto')


if __name__ == '__main__':
    unittest.main()
```

## 5) Métodos setup y teardown

Se usan como auxiliares para cada test que hagamos en nuestra clase

```py
def setUp(self):
    print('>>> El método setUp() se ejecuta antes de cada test')


def tearDown(self):
    print('>>> El método tearDown() se ejecuta después de cada test')
```

Tambien tenemos métodos de clase que nos ayuda a que se ejecuten antes y después de todas las pruebas:

```py
@classmethod
def setUpClass(cls):
    print('>>> El metodo de clase setUpClass() se ejecuta antes de todas las pruebas')

@classmethod
def tearDownClass(cls):
    print('>>> El metodo de clase tearDownClass() se ejecuta despues de todas las pruebas')
```

## 6) Métodos assertTrue y assertFalse

```py
def setUp(self):
    self.name = 'iPhone'
    self.price = 500.00
    self.smarthphone = Product(self.name, self.price)
    self.shopping_cart_1 = ShoppingCart()
    self.shopping_cart_2 = ShoppingCart()
    self.shopping_cart_2.add_product(self.smarthphone)


def test_shopping_cart_empty(self):
    self.assertTrue(self.shopping_cart_1.empty(), 'El carrito de compras no esta vacio')


def test_shopping_has_product(self):
    self.assertFalse(self.shopping_cart_1.has_products(), 'El carrito de compras tiene productos')
    self.assertTrue(self.shopping_cart_2.has_products(), 'El carrito de compras no tiene productos')
```

## 7) Métodos AssertIn y AssertNotIn

```py
def test_products_in_shopping_cart(self):
    self.assertIn(self.smarthphone, self.shopping_cart_2.products, 'El producto no esta en el carrito de compras')

    product = Product('Laptop', 1000.00)
    self.shopping_cart_2.add_product(product)

    self.assertIn(product, self.shopping_cart_2.products, 'El producto no esta en el carrito de compras')


def test_product_not_in_shopping_cart(self):
    self.shopping_cart_2.remove_product(self.smarthphone)
    self.assertNotIn(self.smarthphone, self.shopping_cart_2.products, 'El producto esta en el carrito de compras')
```

## 8) Método AssertRaise

```py
# Nueva clase de error en products.py
class ProductDiscountError(Exception):
    pass


# Dentro del constructor de Product
if discount > price:
    raise ProductDiscountError('El descuento no puede ser mayor al precio del producto')


# Nuevo test
def test_discount_error(self):
    with self.assertRaises(ProductDiscountError):
        Product(name='Laptop', price=1000.00, discount=2000.00)
```

## 9) Métodos operadores relacionales

```py
@property
def total(self) -> float:
    return sum([(product.price - product.discout) for product in self.__products])


def test_total_shopping_cart(self):
    self.shopping_cart_1.add_product(Product(name='Libro', price=100.00))
    self.shopping_cart_1.add_product(Product(name='Laptop', price=1000.00, discount=200.00))

    self.assertGreater(self.shopping_cart_1.total, 0, 'El total del carrito de compras no es correcto')
    self.assertLess(self.shopping_cart_1.total, 1000.00, 'El total del carrito de compras no es correcto')
    # assertGreaterEqual
    # assertLessEqual
    self.assertEqual(self.shopping_cart_1.total, 900.00, 'El total del carrito de compras no es correcto')
```

## 10) Saltar pruebas unitarias

Existen dos casos:

1. El desarrollador sabe que una prueba no puede ejecutarse
2. El desarrollador no sabe o no puede si puede ejecutar una prueba (por factores externos)

```py
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
```

## 11) Validar expresiones regulares

```py
def test_code_product(self):
    self.assertRegex(self.smarthphone.code, r'^code-.*$', 'El codigo del producto no es correcto')
```

## 12) Modularizar pruebas

```
📦Unittest
┣ 📂entities
┃ ┣ 📂test
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┗ 📜test_product.py
┃ ┃ ┗ 📜test_shopping_cart.py
┃ ┣ 📜__init__.py
┃ ┣ 📜product.py
┃ ┗ 📜shopping_cart.py
┗ 📜main.py
```

```py
# entities/__init__.py
from entities.product import Product
from entities.shopping_cart import ShoppingCart


# Imports de entities/shopping_cart.py
from entities.product import Product


# Imports de entities/test/test_shopping_cart.py
from entities.product import Product, ProductDiscountError
from entities.shopping_cart import ShoppingCart


# Creamos nuevo test_product.py y movemos todas las pruebas de producto
```

```shell
# Ejecutar pruebas especificas
python3 -m unittest entities.test.test_shopping_cart
python3 -m unittest entities.test.test_product


# Ejecutar todas las pruebas
python3 -m unittest discover
```
