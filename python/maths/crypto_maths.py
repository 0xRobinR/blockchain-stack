# modular arithmetic

def forward(base, x, modulus):
    return pow(base, x, modulus)


def inverse(base, target, modulus):
    for x in range(modulus):
        value = pow(base, x, modulus)

        print(f"x={x:2} -> {value}")

        if value == target:
            print(f"found x = {x}")

    return None


base = 223
power_x = 4
modulus = 17

print("rbase:", base % modulus)

y = forward(base, power_x, modulus)
print("forward:", y)

x = inverse(base, y, modulus)
print("inverse_x:", x)