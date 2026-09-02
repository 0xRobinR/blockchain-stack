package common

import "crypto/sha256"

func ExtractByte(value uint32, position uint32) byte {
	return byte((value >> (position * 8) & 0xFF))
}

func HashBytes(data []byte) [32]byte {
	return sha256.Sum256(data)
}

func NextHash(previous [32]byte, payload []byte) [32]byte {
	combined := make([]byte, 0, len(previous)+len(payload))
	combined = append(combined, previous[:]...)
	combined = append(combined, payload...)

	return HashBytes(combined)
}
