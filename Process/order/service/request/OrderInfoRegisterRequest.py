from dataclasses import dataclass

from order.entity.Order import ProductOrder

@dataclass
class OrderInfoRegisterRequest:
    __accountId: int
    __productId: int

    def __init__(self, accountId: int, productId: int):
        self.__accountId = accountId
        self.__productId = productId

    def getAccountId(self):
        return self.__accountId

    def toOrder(self):
        return ProductOrder(self.__accountId, self.__productId)