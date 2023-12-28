from dataclasses import dataclass


@dataclass
class ProductRequestRemove:
    __productId: int

    def getProductId(self):
        return self.__productId