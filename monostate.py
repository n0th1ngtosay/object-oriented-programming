# Моносостояние

class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_attrs # Ссылается на словарь, в каждом экземляре одни свойства


th1 = ThreadData()
th2 = ThreadData()

print(th1.__dict__)
print(th2.__dict__)

th2.id = 3

print(th1.__dict__)
print(th2.__dict__)
