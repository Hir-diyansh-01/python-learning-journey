class employee:
    language = "Python" # This is a class variable.
    salary = 5000000

    def __init__(self, name, salary, language): # This is a Dunder method which is automatically called when an object of the class is created. It is used to initialize the attributes of the object. 
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

hirdiyansh = employee("Hirdiyansh", 100000, "JavaScript") # This will call the __init__ method and print "I am creating an object"
print(hirdiyansh.name, hirdiyansh.salary, hirdiyansh.language) # This will print the name, salary and language of the employee object.