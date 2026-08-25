
# test how encoding works

print(len("₹"))

print(len("₹".encode("utf-8")))

x = 256

print(x.to_bytes(2, "big").hex())

print(x.to_bytes(2, "little").hex())

def test_encode(value: int) -> bytes:
    return value.to_bytes(2, "big")

def encode_from_maths(value: int) -> bytes:
    assert value < 2**256
    high = value // 256
    low = value % 256

    print(high, low)

    return bytes([high, low])

def test_decode(data: bytes) -> int:
    assert len(data) == 2
    return int.from_bytes(data, "big")

print(encode_from_maths(0).hex() == "0000")
print(encode_from_maths(1).hex() == "0001")
print(encode_from_maths(10).hex())
print(encode_from_maths(256).hex() == "0100")
print(encode_from_maths(65535).hex() == "ffff")

try:
    print(encode_from_maths(65536))
except ValueError as e:
    print("I knew it")


assert test_decode(bytes.fromhex("0000")) == 0
assert test_decode(bytes.fromhex("0001")) == 1
assert test_decode(bytes.fromhex("00ff")) == 255
assert test_decode(bytes.fromhex("0100")) == 256
assert test_decode(bytes.fromhex("ffff")) == 65535

# print(test_decode(bytes.fromhex("010000")))

# print(test_decode(b""))
# print(test_decode(b"\x01"))
# print(test_decode(b"\x01\x02\x03"))

def encode_uint16_manual(value: int) -> bytes:
    if value < 0 or value > 0xFFFF:
        raise ValueError("outside uint16 range")

    high = value >> 8
    low = value & 0xFF

    return bytes([high, low])

def decode_uint16_manual(data: bytes) -> int:
    if len(data) != 2:
        raise ValueError("uint16 requires 2 bytes")

    high = data[0]
    low = data[1]

    return (high << 8) | low

assert encode_uint16_manual(0).hex() == "0000"
assert encode_uint16_manual(1).hex() == "0001"
assert encode_uint16_manual(255).hex() == "00ff"
assert encode_uint16_manual(256).hex() == "0100"
assert encode_uint16_manual(258).hex() == "0102"
assert encode_uint16_manual(65535).hex() == "ffff"

assert decode_uint16_manual(bytes.fromhex("0000")) == 0
assert decode_uint16_manual(bytes.fromhex("0001")) == 1
assert decode_uint16_manual(bytes.fromhex("00ff")) == 255
assert decode_uint16_manual(bytes.fromhex("0100")) == 256
assert decode_uint16_manual(bytes.fromhex("0102")) == 258
assert decode_uint16_manual(bytes.fromhex("ffff")) == 65535

for value in range(65536):
    encoded = encode_uint16_manual(value)
    decoded = decode_uint16_manual(encoded)

    assert decoded == value


def extract_byte(value: int, position: int) -> int:
    return (value >> (position * 8)) & 0xFF

value = 0x12345678
assert extract_byte(value, 0) == 0x78
assert extract_byte(value, 1) == 0x56
assert extract_byte(value, 2) == 0x34
assert extract_byte(value, 3) == 0x12


def is_bit_set(value: int, position: int) -> bool:
    return (value & (1 << position)) > 0

value = 0b1010

assert is_bit_set(value, 0) is False
assert is_bit_set(value, 1) is True
assert is_bit_set(value, 2) is False
assert is_bit_set(value, 3) is True

def set_bit(value: int, position: int) -> int:
    return value | (1 << position)

assert set_bit(0b0000, 2) == 0b0100
assert set_bit(0b0001, 2) == 0b0101

def pack_nibbles(high: int, low: int) -> int:
    return (high << 4) | low


assert pack_nibbles(0xA, 0x7) == 0xA7
assert pack_nibbles(0x0, 0xF) == 0x0F
assert pack_nibbles(0xF, 0xF) == 0xFF

def encode_uint16_be(value: int) -> bytes:
    assert (value >= 0 and value <= 0xFFFF)

    high = value >> 8
    low = value & 0xFF

    return bytes([high, low])

assert encode_uint16_be(0x0000).hex() == "0000"
assert encode_uint16_be(0x0001).hex() == "0001"
assert encode_uint16_be(0x00FF).hex() == "00ff"
assert encode_uint16_be(0x0100).hex() == "0100"
assert encode_uint16_be(0x1234).hex() == "1234"
assert encode_uint16_be(0xFFFF).hex() == "ffff"

def encode_uint16_le(value: int) -> bytes:
    assert (value >= 0 and value <= 0xFFFF)

    high = value & 0xFF
    low = value >> 8

    return bytes([high, low])

assert encode_uint16_le(0x1234).hex() == "3412"

def decode_uint16_be(data: bytes) -> int:
    assert len(data) == 2

    high = data[0]
    low = data[1]

    return (high << 8) | low

assert decode_uint16_be(bytes.fromhex("0000")) == 0
assert decode_uint16_be(bytes.fromhex("0100")) == 256
assert decode_uint16_be(bytes.fromhex("1234")) == 0x1234
assert decode_uint16_be(bytes.fromhex("ffff")) == 65535

def decode_uint16_le(data: bytes) -> int:
    assert len(data) == 2

    high = data[1]
    low = data[0]

    return (high << 8) | low

assert decode_uint16_le(bytes.fromhex("3412")) == 0x1234