from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductRequestAdd:
    __name: str
    __price: int
    __info: str

    def __init__(self, name: str, price: int, info: str):
        self.__name = name
        self.__price = price
        self.__info = info

    def toProduct(self):
        return Product(self.__name, self.__price, self.__info)
