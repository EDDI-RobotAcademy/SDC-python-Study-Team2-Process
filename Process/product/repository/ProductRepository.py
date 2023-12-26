import abc


class ProductRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, product):
        pass
    @abc.abstractmethod
    def removeByProductId(self, productId):
        pass

    @abc.abstractmethod
    def edit(self):
        pass

    @abc.abstractmethod
    def list(self):
        pass

    @abc.abstractmethod
    def select(self):
        pass

