from dataclasses import dataclass

@dataclass
class Project:
    name: str
    payment: int
    client: str

class Employee:
    def __init__(self, name, age, salary, project):
       self.name = name
       self.age = age
       self.salary = salary
       self.project = project

project = Project("Django app", "2000", "Globomantics")
employee = Employee("Ji-Soo", 38, 100, project)

print(employee.project)