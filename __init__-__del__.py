class Point():
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y
    
  def __del__(self):
    print("Удаление экземпляра класса: "+str(self))

a = Point(10.20)
print(a.__dict__)

b = Point()
print(b.__dict__)