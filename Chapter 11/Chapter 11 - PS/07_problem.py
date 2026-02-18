class Vector:
    def __init__(self, l):
        self.l = l

    # def __add__(self, other):
    #     return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # def __sub__(self, other):
    #     return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # def __mul__(self, scalar):
    #     return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # def __truediv__(self, scalar):
    #     return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    # def __repr__(self):
    #     return f"Vector({self.x}, {self.y}, {self.z} )"
    
    def __len__(self):
        return len(self.l)
    

# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))  # Output: 3

