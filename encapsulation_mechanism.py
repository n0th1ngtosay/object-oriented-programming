# pip install accessify

class Point():
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls,x):
        return type(x) in (int,float)


    def set_coords(self,x,y): # Сеттер
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Должны быть числа')

    def get_coords(self): # Геттер
        return self.__x, self.__y

pt = Point(1,2)
# print(pt.__x)

pt.set_coords(3,2)
pt.set_coords('3',2)
print(pt.get_coords())

    