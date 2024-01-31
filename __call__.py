# 12 

# При создании экземпляра класса работает метод __call__
# с = Counter(<__call__>)

import math
from typing import Any

class Derivate:
    def __init__(self, func) -> None:
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args: Any, **kwds: Any) -> Any:
        return (self.__fn(x+dx) - self.__fn(x)) / dx
    

@Derivate
def df_sin(x):
    return math.sin(x)

print(df_sin(math.pi/3))
