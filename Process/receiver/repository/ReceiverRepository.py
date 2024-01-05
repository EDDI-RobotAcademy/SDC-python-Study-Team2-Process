import abc


class ReceiverRepository(abc.ABC):
    @abc.abstractmethod
    def receiveCommand(self, clientSocketObject):
        pass

    @abc.abstractmethod
    def closeSockets(self, clientSocket, transmitQueue):
        pass