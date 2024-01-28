class Point():
  def __new__(cls,*args,**kwargs): # cls - ссылается на класс Point
    print('Вызов __new__ для '+str(cls))
    return super().__new__(cls) # возвращаем адрес нового объекта

  def __init__(self,x=0,y=0): # self - ссылается на экземпляр
    print('Вызов __init__ для '+str(self))
    self.x = x
    self.y = y

pt = Point(1,2)
print(pt)
