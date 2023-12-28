from dataclasses import dataclass


@dataclass
class ProductResponseList:
    __id: int
    __name: str
    __price: int

    def __init__(self, id: int, name: str, price: int):
        self.__id = id
        self.__name = name
        self.__price = price


