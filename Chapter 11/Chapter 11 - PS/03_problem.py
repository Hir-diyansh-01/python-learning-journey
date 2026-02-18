class Employee:
    def __init__(self):
        self.salary = 234
        self._increment = 20   # private variable

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, salary):
        self._increment = ((salary / self.salary) - 1) * 100

    @property
    def salary_after_increment(self):
        return self.salary + (self.salary * self._increment / 100)


e = Employee()

print(e.salary_after_increment)

e.increment = 300   # new salary dena hoga

print(e.increment)
print(e.salary_after_increment)
