import abc


class OrderRepository(abc.ABC):
    @abc.abstractmethod
    def save(self):
        pass

    @abc.abstractmethod
    def save(self, order):
        pass

