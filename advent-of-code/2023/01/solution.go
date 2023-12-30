package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	res, err := solve(parseStringPart1)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Part 1:", res)

	res, err = solve(parseStringPart2)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Part 2:", res)
}

type LineParserFunc func(string) []string

func solve(parser LineParserFunc) (int, error) {
	var res int

	inputFile, err := os.Open("./input.txt")
	if err != nil {
		return res, err
	}
	defer inputFile.Close()

	var results []int
	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		lineResult := parser(scanner.Text())
		n := strings.Join(lineResult, "")
		i, err := strconv.Atoi(n)
		if err != nil {
			return res, err
		}
		results = append(results, i)
	}
	if err := scanner.Err(); err != nil {
		return res, err
	}

	for _, v := range results {
		res += v
	}
	return res, nil
}

func parseStringPart1(s string) []string {
	var first, last rune
	for _, r := range s {
		if unicode.IsDigit(r) {
			if first == 0 {
				first = r
			}
			last = r
		}
	}
	return []string{string(first), string(last)}
}

var spelledDigits = []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

func wordToNumber(s string) string {
	switch s {
	case "one":
		return "1"
	case "two":
		return "2"
	case "three":
		return "3"
	case "four":
		return "4"
	case "five":
		return "5"
	case "six":
		return "6"
	case "seven":
		return "7"
	case "eight":
		return "8"
	case "nine":
		return "9"
	default:
		panic(fmt.Errorf("invalid word: %s", s))
	}
}

func parseStringPart2(s string) []string {
	var first, last string
	for len(s) > 0 {
		r := s[0:1]

		maybeWord := strings.Index("otfsen", string(r))
		if maybeWord > -1 {
			var isWordFound bool
			for _, word := range spelledDigits {
				s, isWordFound = strings.CutPrefix(s, word)
				if isWordFound {
					w := wordToNumber(word)
					if first == "" {
						first = w
					}
					last = w
					break
				}
			}

			if isWordFound {
				continue
			}
		}

		if _, err := strconv.Atoi(r); err == nil {
			if first == "" {
				first = r
			}
			last = r
		}

		if len(s) > 0 {
			s = s[1:]
		}
	}

	return []string{first, last}
}
