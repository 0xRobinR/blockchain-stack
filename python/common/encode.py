
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

print(test_decode(b""))
print(test_decode(b"\x01"))
print(test_decode(b"\x01\x02\x03"))