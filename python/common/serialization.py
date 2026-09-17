from dataclasses import dataclass
from encode import encode_uint16_be, encode_uint8, decode_uint16_be, hash_bytes
@dataclass
class Transaction:
    version: int
    from_adr: int
    to_adr: int
    amount: int
    nonce: int

def serialize_txn(txn: Transaction) -> bytes:
    version = encode_uint8(txn.version)
    nonce = encode_uint16_be(txn.nonce)
    from_adr = encode_uint16_be(txn.from_adr)
    to_adr = encode_uint16_be(txn.to_adr)
    amount = encode_uint16_be(txn.amount)
    return version + from_adr + to_adr + amount + nonce

tx = Transaction(
    version=1,
    from_adr=42,
    to_adr=91,
    amount=500,
    nonce=7,
)

serialized_tx = serialize_txn(tx)

assert isinstance(serialized_tx, bytes)
assert len(serialized_tx) == 9
assert serialized_tx.hex() == "01002a005b01f40007"

def deserialize_txn(data: bytes) -> Transaction:
    assert len(data) == 9

    version = data[0]
    from_adr = data[1:3]
    to_adr = data[3:5]
    amount = data[5:7]
    nonce = data[7:9]

    return Transaction(
        version=int(version),
        from_adr=decode_uint16_be(from_adr),
        to_adr=decode_uint16_be(to_adr),
        amount=decode_uint16_be(amount),
        nonce=decode_uint16_be(nonce),
    )


decoded_tx = deserialize_txn(serialized_tx)
assert decoded_tx == tx

def txn_hash(serialized_tx: bytes) -> str:
    return hash_bytes(serialized_tx).hex()

print(txn_hash(serialized_tx))

original_tx = serialized_tx

corrupted = bytearray(original_tx)
corrupted[6] ^= 0x05
print(txn_hash(bytes(corrupted)))
print(deserialize_txn(bytes(corrupted)))

def signing_digest(txn: Transaction) -> bytes:
    serialized_txn = serialize_txn(txn)
    return hash_bytes(serialized_txn)

tx1 = Transaction(
    version=1,
    from_adr=42,
    to_adr=91,
    amount=500,
    nonce=7,
)

tx2 = Transaction(
    version=1,
    from_adr=42,
    to_adr=91,
    amount=501,
    nonce=7,
)

print(signing_digest(tx1))
assert len(signing_digest(tx1)) == 32

assert signing_digest(tx1) == signing_digest(tx1)

assert signing_digest(tx1) != signing_digest(tx2)
