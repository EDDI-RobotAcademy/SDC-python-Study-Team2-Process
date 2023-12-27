from dataclasses import dataclass


@dataclass
class ProductRequestFind:
    __productId: int

    def getProductId(self):
        return self.__productId