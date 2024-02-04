# 18

class Student:
    def __init__(self,name,marks) -> None:
        self.name = name
        self.marks = (list(marks))

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")
        
    def __setitem__(self,key,value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индексы должен быть целым неотрицательным числом")
        
        if key >= len(self.marks): # Расширение списка
            off = key+1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self,key):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индексы должен быть целым неотрицательным числом")
        
        del self.marks[key]

s1 = Student("Сергей", [5,5,3,2,4])
# s1[10] = 4
del s1[2]
print(s1.marks)

