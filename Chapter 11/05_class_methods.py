class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 32
e.show()  # Output: The class value of a is 32