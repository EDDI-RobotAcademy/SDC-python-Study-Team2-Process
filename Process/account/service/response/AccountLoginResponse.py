from dataclasses import dataclass


@dataclass
class AccountLoginResponse:
    __sessionAccountId: int
    __message: str

    def __init__(self, sessionAccountId: int, message: str = "로그인 성공"):
        self.__sessionAccountId = sessionAccountId
        self.__message = message

    def __iter__(self):
        yield "__sessionAccountId", self.__sessionAccountId
        yield "__message", self.__message

    def getSessionAccountId(self):
        return self.__sessionAccountId