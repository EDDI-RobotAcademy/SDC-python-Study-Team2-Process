import abc


class OrderService(abc.ABC):
    @abc.abstractmethod
    def orderInfoRegister(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def orderList(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def orderRemove(self, *args, **kwqrgs):
        pass