class ApplicationResponseQuit:
    __protocolNumber = 0


    def __iter__(self):
        yield "__protocolNumber", self.__protocolNumber