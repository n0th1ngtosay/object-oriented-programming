from typing import Any


class Point():
    MAX_COORDS = 100
    MIN_COORDS = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __getattribute__(self, __name: str) -> Any:
        print('__getattribute__')
        return object.__getattribute__(self, __name)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        print('__setattr__')

    def __getattr__(self, item):
        pass

    def __delattr__(self, __name: str) -> None:
        pass


pt1 = Point(1,2)
pt2 = Point(10,20)

a = pt1.x