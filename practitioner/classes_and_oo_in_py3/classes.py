class Employee:
    # improves speed and memory management
    __slots__ = ("name", "age", "salary")
    
    def __init__(self, name, age, salary):
       self.name = name
       self.age = age
       self.salary = salary

    # @property
    # def salary(self):
    #     return self._salary
    
    # @salary.setter
    # def salary(self, salary):
    #     if salary < 1000:
    #         raise ValueError('Minimum wage is $1000')
    #     self._salary = salary

    # @property
    # def annual_salary(self):
    #     return self.salary * 12

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

    def __str__(self):
        return (f"{self.name} is {self.age} years old. Employee is a --- with the salary of ${self.salary}")
    
    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.salary)})"
    
class Tester(Employee):
    def run_tests(self):
        print(f"Testsing started by {self.name}...")
        print("Tests are done.")

class Developer(Employee):
    __slots__ = ("framework", )

    def __init__(self, name, age, salary, framework):
       super().__init__(name, age, salary)
       self.framework = framework
    
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus


tester = Tester("Lauren", 44, 1000)
developer = Developer("Ji-Soo", 38, 1000, "C#")

tester.increase_salary(20)
developer.increase_salary(20, 30)

print(tester.salary)
print(developer.salary)
