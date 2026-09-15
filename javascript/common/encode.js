const assert = require("assert")

function encodeUint16(a) {
    if (!Number.isInteger(a) || a < 0 || a > 0xffff) {
        throw new Error("require uint16")
    }

    high = a >> 8
    low = a & 0xff

    return Buffer.from([high, low])
}

assert.strictEqual(encodeUint16(0).toString("hex"), "0000")
assert.strictEqual(encodeUint16(1).toString("hex"), "0001")
assert.strictEqual(encodeUint16(255).toString("hex"), "00ff")
assert.strictEqual(encodeUint16(256).toString("hex"), "0100")
assert.strictEqual(encodeUint16(258).toString("hex"), "0102")
assert.strictEqual(encodeUint16(65535).toString("hex"), "ffff")

console.log("All tests passed")