package main

import (
	"fmt"
)

func normalize(str []rune) []rune {
	// Index to keep track of the current position where non-space characters should be placed
	writeIndex := 0
	// Flag to track if the previous character was a space
	prevSpace := false

	for _, char := range str {
		if char == ' ' {
			if !prevSpace {
				// If the current character is a space and the previous character was not a space,
				// replace it with a single space
				str[writeIndex] = ' '
				writeIndex++
				prevSpace = true
			}
		} else {
			// If the current character is not a space, copy it to the writeIndex position
			str[writeIndex] = char
			writeIndex++
			prevSpace = false
		}
	}

	// Resize the rune slice to truncate any extra characters after the last non-space character
	str = str[:writeIndex]
	return str
}

func main() {
	// Example 1
	str1 := []rune("a   b  c  ")
	fmt.Println("Original string 1:", string(str1))
	fmt.Printf("(str1): %#v\n", str1)

	fmt.Println("len", len(str1), "cap", cap(str1))
	result1 := normalize(str1)

	fmt.Printf("(result1): %#v\n", result1)
	fmt.Println("len", len(result1), "cap", cap(result1))
	fmt.Println("String with single spaces:", string(result1))

	fmt.Println()

	// Example 2
	str2 := []rune("    a     ")
	fmt.Println("Original string 2:", string(str2))
	result2 := normalize(str2)
	fmt.Println("String with single spaces:", string(result2))
}
