class Employee:
    def __init__(self):
        print("Employee class constructor called")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Programmer class constructor called")
    b = 2

class Coder(Programmer):
    def __init__(self):
        super().__init__()
        print("Coder class constructor called")
    c = 3

o = Coder()
print(o.a, o.b, o.c)