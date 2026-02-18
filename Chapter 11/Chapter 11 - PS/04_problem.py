class Complex:
     def __init__(self, real, imag):
         self.real = real
         self.imag = imag

     def __add__(self, c2):
         return Complex(self.real + c2.real, self.imag + c2.imag)
        
c1 = Complex(1, 2)
c2 = Complex(3, 4)
c3 = c1 + c2 
print(f"Sum of complex numbers: {c3.real} + {c3.imag}j")