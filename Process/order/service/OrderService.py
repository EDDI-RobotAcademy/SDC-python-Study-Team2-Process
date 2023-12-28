import abc


class OrderService(abc.ABC):
    @abc.abstractmethod
    def productBuy(self, *args, **kwargs):
        pass
