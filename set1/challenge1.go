package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

func convertToBase64(hex_data string) string {
	// Convert hex to bytes
	decoded, err := hex.DecodeString(hex_data)
	if err != nil {
		fmt.Println("Error decoding hex:", err)
		return ""
	}
	// Convert to base64
	base64Output := base64.StdEncoding.EncodeToString(decoded)
	return base64Output
}

func main() {
	var text = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

	converted := convertToBase64(text)
	fmt.Println(converted)
}
