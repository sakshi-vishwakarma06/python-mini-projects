#Employee Management system
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        
    
    @abstractmethod
    def calculate_bonus(self):
        pass
    def get_salary(self):
        return self.__salary
class Manager(Employee):
    def calculate_bonus(self):
        return self.get_salary()*0.20
class Developer(Employee):
    def calculate_bonus(self):
        return  self.get_salary()*0.10

#ask Employee type
emp_type=input("Enter employee type(Developer/manager):").lower()
name=input("Enter your name:")
salary=float(input(("Enter your salary:")))
if emp_type=="manager":
    emp=Manager(name,salary)
elif emp_type=="developer":
    emp=Developer(name,salary)
else:
    print("Invalid employee type.")
    exit()

print("Name:",emp.name)
print("Salary",emp.get_salary())
print("Bonus:",emp.calculate_bonus())

        


