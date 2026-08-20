
# test how encoding works

print(len("₹"))

print(len("₹".encode("utf-8")))

x = 256

print(x.to_bytes(2, "big").hex())

print(x.to_bytes(2, "little").hex())

def test_encode(value: int) -> bytes:
    return value.to_bytes(2, "big")


print(test_encode(0).hex() == "0000")
print(test_encode(1).hex() == "0001")
print(test_encode(255).hex() == "00ff")
print(test_encode(256).hex() == "0100")
print(test_encode(65535).hex() == "ffff")

try:
    print(test_encode(65536))
except Exception as e:
    print("I knew it")