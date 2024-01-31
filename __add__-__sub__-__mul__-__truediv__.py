# 14
# Операция сложения, вычитания, умножения, деления

class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self,seconds:int) -> None:
        if not isinstance(seconds,int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self. seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")
    
    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int")
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)
    
    def __radd__(self, other): # c1 = 100 + c1
        return self + other
    
    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self  

c1 = Clock(1000)
c1 = c1 + 100 # c1.__add__(100)
print(c1.get_time())

c2 = Clock(1000)
c3 = Clock(2000)
c4 = c2 + c3
print(c4.get_time())

c5 = Clock(1000)
c5 += 100
print(c5.get_time())