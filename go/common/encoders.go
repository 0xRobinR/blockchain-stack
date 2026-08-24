package common

func ExtractByte(value uint32, position uint32) byte {
	return byte((value >> (position * 8) & 0xFF))
}
