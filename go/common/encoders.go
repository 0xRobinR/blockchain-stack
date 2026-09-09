package common

import "crypto/sha256"

func EncodeUint16(value uint16) []byte {
	high := value >> 8
	low := value & 0xFF

	return []byte{byte(high), byte(low)}
}

func EncodeUint8(value uint8) []byte {
	return []byte{byte(value)}
}

func DecodeUint16(data []byte) uint16 {
	return uint16(data[0])<<8 | uint16(data[1])
}

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
