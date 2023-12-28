import abc


class ProductService(abc.ABC):
    @abc.abstractmethod
    def productAdd(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def productRemove(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def productInfo(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def productList(self, *args, **kwargs):
        pass
