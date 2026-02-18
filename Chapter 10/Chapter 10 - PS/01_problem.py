class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Hirdiyansh", 100000, 1234)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohit", 200000, 4321)
print(r.name, r.salary, r.pin, r.company)