# 21

class Geom:
    print

class Line(Geom):
    pass

g = Geom()
l = Line()

print(issubclass(Line,Geom)) # (дочерний класс, родительский класс)
print(isinstance(l, Geom))

class Vector(list):
    def __str__(self):
        return " ".join(map(str,self))
    
    # если убрать __str__ ,то вывод будет [1,2,3]
v = Vector([1,2,3])
print(v)