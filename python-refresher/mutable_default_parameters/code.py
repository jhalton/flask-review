from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []): #This is bad! Never make your parameter = to a mutable value
    #you can instead do grades: List[int]: None
        self.name = name
        self.grades = grades #or []
        #if you use the default, self.grades is the name for the specific list defined in this class 

    def take_exam(self, result):
        self.grades.append(result)


willem = Student("Willem")
malcom = Student("Malcom")
willem.take_exam(90)
print(willem.grades)
print(malcom.grades)
#Even though Willem is the only one who took the exam, Malcom is also showing 90. 
