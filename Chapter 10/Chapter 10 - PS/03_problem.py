class Demo:
    a = 4
o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not defined yet
o.a = 0 # Instance attribute is created and assigned the value 0
print(o.a) # Prints the instance attribute which is 0
print(Demo.a) # Prints the class attribute which is still 4
