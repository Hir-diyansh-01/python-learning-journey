class employee:
    language = "Python" # This is a class variable.
    salary = 5000000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

hirdiyansh = employee()
hirdiyansh.language = "JavaScript" # This is an instance variable. It is specific to the object hirdiyansh and not shared with other instances of the employee class.
hirdiyansh.getInfo()
employee.greet() # This is how you call a static method. It can be called on the class itself without needing an instance.