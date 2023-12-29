import abc


class OrderService(abc.ABC):
    @abc.abstractmethod
    def orderInfoRegister(self, *args, **kwargs):
        pass
