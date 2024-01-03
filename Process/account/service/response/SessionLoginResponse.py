from dataclasses import dataclass


@dataclass
class SessionLoginResponse:
    __sessionAccountId: int
    __message: str

    def __init__(self, sessionAccountId: int, message: str = "세션 로그인 성공"):
        self.__sessionAccountId = sessionAccountId
        self.__message = message


    def __iter__(self):
        yield "sessionAccountId", self.__sessionAccountId
        yield "message", self.__message
