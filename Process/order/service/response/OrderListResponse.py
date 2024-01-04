from dataclasses import dataclass

@dataclass
class OrderListResponse:
    __name: str
    __price: int

    def __init__(self, name: str, price: int):
        self.__name = name
        self.__price = price

    def __iter__(self):
        # 객체를 iterable로 만들기 위해 __iter__ 메서드를 정의
        yield "name", self.__name
        yield "price", self.__price

    def __dict__(self):
        return {
            "name": self.__name,
            "price": self.__price
        }