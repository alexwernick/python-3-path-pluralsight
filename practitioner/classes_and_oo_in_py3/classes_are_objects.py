from datetime import date

class Employee:

    # I think this is just stored once in memory and not for every instance (liek static in C#)
    minimum_wage = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt.")
        cls.minimum_wage = new_wage

    #example of a factory method or alternative constructor
    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name, age, salary):
       self.name = name
       self.age = age
       self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f"Minimum wage is ${Employee.minimum_wage}")
        self._salary = salary

e = Employee("Ji-Soo", 38, 1000)
e2 = Employee.new_employee("Mary", date(1991, 8, 12))
# shows that everythig is in the dict inlcuing functions. They are just objects of type function
Employee.__dict__["increase_salary"](e, 20)
print(e.salary)
print(e2.age)