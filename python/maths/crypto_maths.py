# modular arithmetic
import random
from math import isqrt

def forward(base, x, modulus):
    return pow(base, x, modulus)


def inverse(base, target, modulus):
    value = 1
    seen = set()

    x = 0

    while value not in seen:
        if value == target:
            return x

        seen.add(value)

        value = (value * base) % modulus
        x += 1

        if x % 1_000_000 == 0:
            print(f"searched {x:,} exponents...")

    return None

def bsgs(base, target, modulus):

    m = isqrt(modulus) + 1
    baby_steps = {}

    value = 1

    for j in range(m):
        if value not in baby_steps:
            baby_steps[value] = j

        value = (value * base) % modulus
    factor = pow(pow(base, m, modulus), -1, modulus)

    gamma = target

    for i in range(m + 1):

        if gamma in baby_steps:
            j = baby_steps[gamma]

            x = i * m + j

            return x

        gamma = (gamma * factor) % modulus

    return None

base = 5
modulus = 1_000_000_007
target = 372_224_738

print("rbase:", base % modulus)

# y = forward(base, power_x, modulus)
# print("forward:", y)

x = bsgs(base, target, modulus)
print("inverse_x:", x)

# rsa lowkey
p = 11
q = 13

n = p * q
phi = (p - 1) * (q - 1)

e = 19

d = pow(e, -1, phi)
print("d:", d)

msg = 93

enc = pow(msg, e, n)
print("enc:", enc)

dec = pow(enc, d, n)
print("dec:", dec)

# diffie-hellman lowkey
pub_p = 23
pub_g = 7

a_sec = 19
b_sec = 29

a_pub = pow(pub_g, a_sec, pub_p)
b_pub = pow(pub_g, b_sec, pub_p)

print("a_pub:", a_pub)
print("b_pub:", b_pub)

a_shared = pow(b_pub, a_sec, pub_p)
b_shared = pow(a_pub, b_sec, pub_p)

print("a_shared:", a_shared)
print("b_shared:", b_shared)

assert(a_shared == b_shared)

# manual mod ops
def mod_add(a: int, b: int, p: int) -> int:
    return (a + b) % p

def mod_sub(a: int, b: int, p: int) -> int:
    return (a - b) % p

def mod_mul(a: int, b: int, p: int) -> int:
    return (a * b) % p

def mod_pow(a: int, exponent: int, p: int) -> int:
    return pow(a, exponent, p)

def mod_inverse_bruteforce(a: int, p: int) -> int:
    for x in range(1, p):
        if ((a * x) % p) == 1:
            return x


assert mod_add(4, 3, 5) == 2
assert mod_sub(2, 4, 5) == 3
assert mod_mul(4, 3, 5) == 2
assert mod_pow(3, 4, 17) == 13
assert mod_add(100, 50, 7) == 3

assert mod_inverse_bruteforce(3, 7) == 5
assert mod_inverse_bruteforce(2, 7) == 4
assert mod_inverse_bruteforce(6, 7) == 6

# the big prime, p = 2^256 - 2^32 - 977
p = (1 << 256) - (1 << 32) - 977
print("p:", p)

def is_prime_miller_rabin(n: int, k: int = 40) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

print(f"is prime: {is_prime_miller_rabin(p)}")

# using fermats little theorem

def is_prime_fermat(a, p) -> bool:
    return pow(a, p - 1, p) == 1

print(f"is prime: {is_prime_fermat(2, p)}")

# extended euclidean alogrithm

a = 40
b = 17

def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int, int]:
    
    if b == 0:
        return (1, 0, a)
    
    x1, y1, gcd = extended_euclidean_algorithm(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return (x, y, gcd)

x, y, gcd = extended_euclidean_algorithm(a, b)

print(f"gcd({a}, {b}) = {gcd}, x = {x}, y = {y}, {a}*{x} + {b}*{y} = {a*x + b*y}")

def mod_inverse(a: int, m: int) -> int:
    x, y, gcd = extended_euclidean_algorithm(a, m)

    if gcd != 1:
        raise ValueError("Modular inverse does not exist")

    return x % m

print(f"modular inverse: {mod_inverse(b, a)}")

def mod_div(a: int, b: int, p: int) -> int:
    return (a * mod_inverse(b, p)) % p

assert mod_div(4, 3, 7) == 6

def using_fermat_theorem(a: int, p: int) -> int:
    return pow(a, p - 2, p)

assert mod_inverse(3, 7) == using_fermat_theorem(3, 7)
