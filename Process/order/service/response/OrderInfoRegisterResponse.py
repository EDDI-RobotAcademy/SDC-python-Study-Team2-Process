from dataclasses import dataclass

@dataclass
class OrderInfoRegisterResponse:
    __success: bool
    __message: str

    def __init__(self, success: bool, message: str):
        self.__success = success
        self.__message = message

    def __bool__(self):
        return self.__success

    def __dict__(self):
        return {
            "__success": self.__success,
            "__message": self.__message
        }

    def __iter__(self):
        # 객체를 iterable로 만들기 위해 __iter__ 메서드를 정의
        yield "__success", self.__success
        yield "__message", self.__message