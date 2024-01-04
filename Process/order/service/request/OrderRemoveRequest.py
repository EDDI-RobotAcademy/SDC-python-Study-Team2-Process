#accounntreposi, productreposi 다 가져오기
from dataclasses import dataclass

@dataclass
class OrderRemoveRequest:
    __sessionId: int
    __productId: int

    def __init__(self, sessionId: int, productId: int):
        self.__sessionId = sessionId
        self.__productId = productId

    def getSessionId(self):
        return self.__sessionId

    def getProductId(self):
        return self.__productId