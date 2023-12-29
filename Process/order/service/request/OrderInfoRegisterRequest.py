from dataclasses import dataclass

from order.entity.Order import ProductOrder

@dataclass
class OrderInfoRegisterRequest:
    __sessionId: int
    __productId: int

    def __init__(self, sessionId: int, productId: int):
        self.__sessionId = sessionId
        self.__productId = productId

    def getSessionId(self):
        return self.__sessionId

    def toOrder(self):
        return ProductOrder(self.__sessionId, self.__productId)