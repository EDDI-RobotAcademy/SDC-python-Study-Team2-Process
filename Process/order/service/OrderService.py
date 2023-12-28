import abc


class OrderService(abc.ABC):
    @abc.abstractmethod
    def addOrderInfo(self, *args, **kwargs):
        pass
