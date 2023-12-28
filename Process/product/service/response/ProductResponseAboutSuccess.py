from dataclasses import dataclass


@dataclass
class ProductResponseAboutSuccess:
    __success: bool
    __message: str

    def __init__(self, success: bool, message: str):
        self.__success = success
        self.__message = message

    def __bool__(self):
        return self.__success

    def __dict__(self):
        return {
            "success": self.__success,
            "message": self.__message
        }

    def __iter__(self):
        # 객체를 iterable로 만들기 위해 __iter__ 메서드를 정의
        yield "success", self.__success
        yield "message", self.__message