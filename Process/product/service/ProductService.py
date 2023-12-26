
import abc

class ProductService(abc.ABC):
    @abc.abstractmethod
    def productAdd(self, *args, **kwargs):
        pass