"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""


class Quaternion:
    """ q = s + xi + yj + zk, s,x,y,z ∈ ℝ  and i^2 = j^2 = k^2 = ijk = -1 """

    def __init__(self, s, x, y, z):
        self.s = s
        self.x = x
        self.y = y
        self.z = z
        self.norm = (self.s * self.s + self.x * self.x + self.y * self.y + self.z * self.z) ** (1 / 2)

    def __add__(self, other):
        return Quaternion(self.s + other.s, self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Quaternion(self.s - other.s, self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        s = self.s * other.s - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.s * other.x + other.s * self.x + self.y * other.z - other.y * self.z
        y = self.s * other.y + other.s * self.y + self.z * other.x - other.z * self.x
        z = self.s * other.z + other.s * self.z + self.x * other.y - other.x * self.y
        return Quaternion(s, x, y, z)

    def __truediv__(self, other):
        return self * other.reciprocal()

    def __lt__(self, other):
        return self.norm < other.norm

    def __le__(self, other):
        return self.norm <= other.norm

    def __eq__(self, other):
        return self.norm == other.norm

    def __ne__(self, other):
        return self.norm != other.norm

    def __gt__(self, other):
        return self.norm > other.norm

    def __ge__(self, other):
        return self.norm >= other.norm

    def __abs__(self):
        return self.norm

    def __str__(self):
        return f"{self.s:+}{self.x:+}*i{self.y:+}*j{self.z:+}*k"

    def __repr__(self):
        return f'Quaternion({self.s}, {self.x}, {self.y}, {self.z})'

    def reciprocal(self):
        s = self.conjugate().s / (self.norm ** 2)
        x = self.conjugate().x / (self.norm ** 2)
        y = self.conjugate().y / (self.norm ** 2)
        z = self.conjugate().z / (self.norm ** 2)
        return Quaternion(s, x, y, z)

    def conjugate(self):
        return Quaternion(self.s, -self.x, -self.y, -self.z)


if __name__ == "__main__":
    q = Quaternion(1, 4, 4, -4)
    qu = Quaternion(1, 4, 4, -4)
    print(q)
    print(q + qu)
    print(q * qu)
    print(q / qu)
    print(q == qu)
    print(abs(q))
    print(repr(q))
    print(q.conjugate())
    print(q.reciprocal())
