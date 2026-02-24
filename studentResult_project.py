#Student result management system
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculate_grade(self):
        if self.marks>90:
            return "A+"
        elif self.marks>=80:
            return "A"
        elif self.marks>=60:
            return "B"
        elif self.marks>=40:
            return "C"
        else:
            return "Fail"
        
    def display_result(self):
        grade=self.calculate_grade()
        print(f"{self.name} scored {self.marks} and got grade {grade}")


#list to store students
students=[]

#Ask total number of students
n=int(input("Enter the number of students:"))

#Add students
for i in range(n):
    name=input("Enter your name:")
    marks=int(input("Enter your marks:"))
    students.append(Student(name,marks))
print()   #for space
 
print("-----Result-----")

for student in students:
    student.display_result()