from dataclasses import dataclass

@dataclass
class OrderListRequest:
    __sessionId: int

    def __init__(self, sessionId: int):
        self.__sessionId = sessionId

    def getSessionId(self):
        return self.__sessionId