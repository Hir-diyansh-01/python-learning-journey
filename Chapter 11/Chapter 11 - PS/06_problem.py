class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __repr__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)    
v3 = Vector(7, 8, 9)

print(v1 + v2)  # Vector(5, 7, 9)
print(v1 - v2)  # Vector(-3, -3, -3)
print(v1 * 2)   # Vector(2, 4, 6)
print(v1 / 2)   # Vector(0.5, 1.0, 1.5)
print(v1 + v2 + v3)  # Vector(12, 15, 18)
