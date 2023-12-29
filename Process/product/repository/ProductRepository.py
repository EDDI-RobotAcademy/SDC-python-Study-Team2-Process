import abc


class ProductRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, product):
        pass

    @abc.abstractmethod
    def removeByProductId(self, request):
        pass

    @abc.abstractmethod
    def edit(self, request):
        pass

    @abc.abstractmethod
    def findAllProducts(self):
        pass

    @abc.abstractmethod
    def findById(self, request):
        pass

