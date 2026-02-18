class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")

    def Cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")

    def squareroot(self):
        print(f"The square root of {self.n} is {self.n ** 0.5}")

    @staticmethod
    def greet():
        print("Welcome to the Calculator!") 

a = Calculator(5)
a.square()  
a.Cube()
a.squareroot()
a.greet()