class employee:
    company = "Google"
    name = "default name"  
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language is {self.language}")


class programmer(employee, Coder):
    company = "Microsoft"
    def showLanguage(self):    
        print(f"The name is {self.company} and the language is {self.language}")

a = employee()
b = programmer()

b.show()
b.printLanguage()
b.showLanguage()