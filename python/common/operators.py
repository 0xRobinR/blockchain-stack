def and_op(a: int, b: int) -> int:
    return a & b

def or_op(a: int, b: int) -> int:
    return a | b

def left_shift(value: int) -> int:
    return value << 8 # value * 2**8

def right_shift(value: int) -> int:
    return value >> 8 # value / 2**8

def xor_op(a: int, b: int) -> int:
    c = a ^ b
    original = c ^ b

    print(c, original)

a = 223
b = 110

print(and_op(a, b))
print(or_op(a, b))
print(left_shift(a))
print(right_shift(a))

xor_op(a, b)