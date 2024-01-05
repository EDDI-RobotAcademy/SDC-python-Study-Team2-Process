from dataclasses import dataclass


@dataclass
class ApplicationRequestQuit:
    __accountSessionId: int

    def getAccountSessionId(self):
        return self.__accountSessionId