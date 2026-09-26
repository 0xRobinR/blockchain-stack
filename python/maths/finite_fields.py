
class FiniteField:
    def __init__(self, value: int, prime: int):
        self.value = value
        self.prime = prime
    
    def __add__(self, other):
        assert self.prime == other.prime, "primes must be equal"
        add_value = self.value + other.value

        return FiniteField(add_value % self.prime, self.prime)
    
    def __sub__(self, other):
        assert self.prime == other.prime, "primes must be equal"
        sub_value = self.value - other.value

        return FiniteField(sub_value % self.prime, self.prime)
    
    def __mul__(self, other):
        assert self.prime == other.prime, "primes must be equal"
        mul_value = self.value * other.value

        return FiniteField(mul_value % self.prime, self.prime)
    
    def __truediv__(self, other):
        assert self.prime == other.prime, "primes must be equal"
        inv_value = pow(other.value, self.prime - 2, self.prime)
        mul_value = self.value * inv_value

        return FiniteField(mul_value % self.prime, self.prime)

    



a = FiniteField(5, 7)
b = FiniteField(4, 7)

c = a + b

assert c.value == 2
assert c.prime == 7

c = a - b

assert c.value == 1

c = a * b
assert c.value == 6

a = FiniteField(4, 7)
b = FiniteField(3, 7)

c = a / b

assert c.value == 6
