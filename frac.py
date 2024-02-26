class Frac:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self._simplify()

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def _simplify(self):
        gcd = self._gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Frac(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Frac(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Frac(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Frac(new_num, new_den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self.num * other.den <= other.num * self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self.num * other.den >= other.num * self.den

    def __str__(self):
        return f"{self.num}/{self.den}"
