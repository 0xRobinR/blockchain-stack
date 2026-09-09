package common

type Transaction struct {
	Version uint8
	FromAdr uint16
	ToAdr   uint16
	Amount  uint16
	Nonce   uint16
}

func SerializeTx(transaction Transaction) []byte {
	data := make([]byte, 0, 9)

	data = append(data, EncodeUint8(transaction.Version)...)
	data = append(data, EncodeUint16(transaction.FromAdr)...)
	data = append(data, EncodeUint16(transaction.ToAdr)...)
	data = append(data, EncodeUint16(transaction.Amount)...)
	data = append(data, EncodeUint16(transaction.Nonce)...)

	return data
}

func DecodeTx(data []byte) Transaction {
	version := data[0]
	from_adr := data[1:3]
	to_adr := data[3:5]
	amount := data[5:7]
	nonce := data[7:9]

	return Transaction{
		Version: version,
		FromAdr: DecodeUint16(from_adr),
		ToAdr:   DecodeUint16(to_adr),
		Amount:  DecodeUint16(amount),
		Nonce:   DecodeUint16(nonce),
	}
}
