class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Coder(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the attribute 
# print(o.b) # Throws an error because b is not an attribute of Employee

o = Programmer()
print(o.a) # Prints the attribute a because it is inherited from Employee
print(o.b) # Prints the attribute b because it is an attribute of Programmer

o = Coder()
print(o.a) # Prints the attribute a because it is inherited from Employee
print(o.b) # Prints the attribute b because it is inherited from Programmer
print(o.c) # Prints the attribute c because it is an attribute of Coder