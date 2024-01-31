class Person:
    def __init__(self,name,old) -> None:
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self,old):
        self.__old = old

    # В приоритете
    # old = property(get_old, set_old)
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)
        
    @old.deleter
    def old(self):
        del self.__old

p = Person('Сергей', 20)
p.old = 35
del p.old
print(p.old, p.__dict__)

