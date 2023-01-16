from entities.product import Product


class ShoppingCart:
    
    def __init__(self) -> None:
        # self.__products = list()
        self.__products: list[Product] = []
    

    @property
    def products(self) -> list[Product]:
        return self.__products.copy()


    @property    
    def total(self) -> float:
        return sum([(product.price - product.discout) for product in self.__products])


    def add_product(self, product: Product) -> None:
        assert isinstance(product, Product), 'El producto debe ser de tipo Product'
        self.__products.append(product)


    def empty(self) -> bool:
        return len(self.__products) == 0
    

    def has_products(self):
        return not self.empty()

    
    def remove_product(self, product: Product) -> None:
        assert isinstance(product, Product), 'El producto debe ser de tipo Product'
        self.__products.remove(product)