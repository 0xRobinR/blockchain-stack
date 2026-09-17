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
