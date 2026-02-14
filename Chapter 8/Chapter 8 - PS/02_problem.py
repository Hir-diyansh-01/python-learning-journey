def f_to_c(f):
   return (f - 32) * 5.0/9.0

f = int(input("Enter a temperature in Fahrenheit: "))
print(f"{f_to_c(f)} degrees Celsius")