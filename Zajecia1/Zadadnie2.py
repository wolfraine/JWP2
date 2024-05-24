import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

    @staticmethod
    def are_orthogonal(v1, v2):
        return v1.dot(v2) == 0


v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(v1)  # Output: Vector3D(1, 2, 3)
print(v2.norm())  # Output: Długość wektora v2
print(v1 + v2)  # Output: Vector3D(5, 7, 9)
print(v1 - v2)  # Output: Vector3D(-3, -3, -3)
print(v1 * 3)  # Output: Vector3D(3, 6, 9)
print(v1.dot(v2))  # Output: Iloczyn skalarny v1 i v2
print(v1.cross(v2))  # Output: Vector3D(-3, 6, -3)
print(Vector3D.are_orthogonal(v1, v2))  # Output: False (ponieważ nie są ortogonalne)
