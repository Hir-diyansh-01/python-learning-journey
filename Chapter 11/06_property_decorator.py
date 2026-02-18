class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    @property
    def name(self):
        return self.enam
    
    @name.setter
    def name(self, value):
        self.enam = value

e = Employee()
e.a = 32

e.name = "Hirdiyansh"
print(e.name)  # Output: Hirdiyansh
e.show()  # Output: The class value of a is 32