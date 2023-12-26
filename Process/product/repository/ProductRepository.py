import abc


class ProductRepository():

    @abc.abstractmethod
    def add(self, _product):
        pass
    @abc.abstractmethod
    def remove(self):
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

