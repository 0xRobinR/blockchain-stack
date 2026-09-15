const crypto = require("crypto")

const { publicKey: pubkey, privateKey: privkey } = crypto.generateKeyPairSync("rsa", {
    modulusLength: 2048
})

const message = "gibberish gibberish xx yy zz"

const signature = crypto.sign(
    "sha256",
    Buffer.from(message, "utf8"),
    privkey
)

console.log("Signature:", signature.toString("hex"))

const valid = crypto.verify(
    "sha256",
    Buffer.from(message, "utf8"),
    pubkey,
    signature
)

console.log("Valid:", valid)