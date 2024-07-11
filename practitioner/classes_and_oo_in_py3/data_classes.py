from dataclasses import dataclass

# can set slots in the attribute
@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

# you can still add functions to dataclasses. They are in fact just classes with some tidy up of syntax I think
def notidy_client(self):
    print(f"Notifying the client about the progress of the {self.name}...")

class Employee:
    def __init__(self, name, age, salary, project):
       self.name = name
       self.age = age
       self.salary = salary
       self.project = project

project = Project("Django app", 2000, "Globomantics")
employee = Employee("Ji-Soo", 38, 100, project)

print(employee.project)