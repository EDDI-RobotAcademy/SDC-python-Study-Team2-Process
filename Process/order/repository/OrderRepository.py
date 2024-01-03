import abc


class OrderRepository(abc.ABC):

    @abc.abstractmethod
    def saveOrderInfo(self, orderInfo):
        pass

    @abc.abstractmethod
    def findAccountId(self, accountId):
        pass

    @abc.abstractmethod
    def removeProductsByAccountId(self, sessionId, productId):
        pass