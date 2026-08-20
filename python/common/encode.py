
# test how encoding works

print(len("₹"))

print(len("₹".encode("utf-8")))

x = 256

print(x.to_bytes(2, "big").hex())

print(x.to_bytes(2, "little").hex())

def test_encode(value: int) -> bytes:
    return value.to_bytes(2, "big")

def test_decode(data: bytes) -> int:
    return int.from_bytes(data)

print(test_encode(0).hex() == "0000")
print(test_encode(1).hex() == "0001")
print(test_encode(255).hex() == "00ff")
print(test_encode(256).hex() == "0100")
print(test_encode(65535).hex() == "ffff")

try:
    print(test_encode(65536))
except Exception as e:
    print("I knew it")


assert test_decode(bytes.fromhex("0000")) == 0
assert test_decode(bytes.fromhex("0001")) == 1
assert test_decode(bytes.fromhex("00ff")) == 255
assert test_decode(bytes.fromhex("0100")) == 256
assert test_decode(bytes.fromhex("ffff")) == 65535

print(test_decode(bytes.fromhex("010000")))