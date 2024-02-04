# 17

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y
    
    def __bool__(self): # В приоритете
        print("__bool__")
        return self.x == self.y
    
p = Point(1,10) # (1,1)

if p:
    print("Объект p дает True")
else:
    print("Объект p дает False")