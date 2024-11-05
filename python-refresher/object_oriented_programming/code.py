# student = {"name": 'Jude', "grades": (89, 90, 93, 100, 90)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Willem", (89, 90, 98, 100, 91))
student2 = Student("Jude", (100, 100, 100, 102, 100))
print(student.name)
print(student.grades)
print(student.average_grade())

print(student2.name)
print(student2.grades)
print(student2.average_grade())
