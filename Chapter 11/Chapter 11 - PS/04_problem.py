class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c2):
        return Complex(self.real + c2.real, self.imag + c2.imag)

    def __mul__(self, c2):
        real_part = self.real * c2.real - self.imag * c2.imag
        imag_part = self.real * c2.imag + self.imag * c2.real
        return Complex(real_part, imag_part)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}j"
        else:
            return f"{self.real} - {abs(self.imag)}j"


c1 = Complex(1, 2)
c2 = Complex(3, 4)

c3 = c1 + c2
print("Sum:", c3)

c4 = c1 * c2
print("Product:", c4)
