# modular arithmetic
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
