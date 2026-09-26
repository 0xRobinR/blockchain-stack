package maths

func ModAdd(a, b, p uint64) uint64 {
	return (a + b) % p
}

func ModSub(a, b, p uint64) uint64 {
	return (a - b) % p
}

func ModMul(a, b, p uint64) uint64 {
	return (a * b) % p
}

func ModInverseBruteforce(a, p uint64) uint64 {
	for x := uint64(1); x < p; x++ {
		if (a*x)%p == 1 {
			return x
		}
	}
	return 0
}
