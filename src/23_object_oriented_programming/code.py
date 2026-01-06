class Student:
    def __init__(self,name, grades):
        self.name = name
        self.grades = grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob",(90,56,54,68,89))
print(student.name)
print(student.grades)
print(Student.average_grade(student)) # as class
print(student.average_grade()) # as object 

student2 = Student("Rolf",(100,100,100,100,99))
print(student2.name)
print(student2.grades)
print(Student.average_grade(student2)) # as class
print(student2.average_grade()) # as object 