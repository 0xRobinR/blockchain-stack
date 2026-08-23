
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
except Exception as e:
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