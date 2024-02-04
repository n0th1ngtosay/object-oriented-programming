class Geo():
    def __init__(self,x1,x2,y1,y2):
        print(f"Инициализатор Geo для класса {self.__class__}")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Line(Geo):
    def drow(self):
        print("Рисование линии")

class Rect(Geo):
    def __init__(self, x1, x2, y1, y2,fill=None):
        super().__init__(x1, x2, y1, y2) # Называется делегирование
        print("Инициализатор Rect")
        self.fill = fill

    def drow(self):
        print("Рисование прямоугольника")

l = Line(0,0,10,20)
r = Rect(1,2,3,4)

print(l.__dict__)
print(r.__dict__)