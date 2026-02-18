class employee:
    language = "Python" # This is a class variable.
    salary = 5000000

hirdiyansh = employee()
hirdiyansh.language = "JavaScript" # This is an instance variable. It is specific to the object hirdiyansh and not shared with other instances of the employee class.
print(hirdiyansh.language, hirdiyansh.salary)

