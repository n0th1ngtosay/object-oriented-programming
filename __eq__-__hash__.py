# 16

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self,other) -> bool: # print(hash(p1), hash(p2), sep="\n") -- работать не будет
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int: # Исправили (хеш не от обьекта,а от координат точки)
        return hash((self.x,self.y))
    
p1 = Point(1,2)
p2 = Point(1,2)

print(hash(p1), hash(p2), sep="\n")
print(p1 == p2)

d = {
}
d[p1] = 1 # Если закомментировать __eq__ и __hash__ то будут разные ключ-значения
d[p2] = 2
print(d)