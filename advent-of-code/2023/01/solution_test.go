package main

import (
	"fmt"
	"reflect"
	"testing"
)

func TestParseStringPart1(t *testing.T) {
	tests := []struct {
		input  string
		output []string
	}{
		{input: "7onetwothree4", output: []string{"7", "4"}},
		{input: "4nineeightseven2", output: []string{"4", "2"}},
		{input: "zoneight234", output: []string{"2", "4"}},
		{input: "treb7uchet", output: []string{"7", "7"}},
	}

	for i, tt := range tests {
		t.Run(fmt.Sprint(i), func(t *testing.T) {
			output := parseStringPart1(tt.input)
			if !reflect.DeepEqual(tt.output, output) {
				t.Errorf("not equal: expected: %+v actual: %+v", tt.output, output)
			}
		})
	}
}

func TestParseStringPart2(t *testing.T) {
	tests := []struct {
		input  string
		output []string
	}{
		{input: "oneb", output: []string{"1", "1"}},
		{input: "onep4b", output: []string{"1", "4"}},
		{input: "onetwothree", output: []string{"1", "3"}},
		{input: "7onetwothree4", output: []string{"7", "4"}},
		{input: "rrzbgtfrrqkspsix3rkpzddzrbcrzvxzstjbqhmqq", output: []string{"6", "3"}},
		{input: "two1nine", output: []string{"2", "9"}},
		{input: "eightwothree", output: []string{"8", "3"}},
		{input: "abcone2threexyz", output: []string{"1", "3"}},
		{input: "xtwone3four", output: []string{"2", "4"}},
		{input: "4nineeightseven2", output: []string{"4", "2"}},
		{input: "zoneight234", output: []string{"1", "4"}},
		{input: "7pqrstsixteen", output: []string{"7", "6"}},
		{input: "sixsixqbksfrndvg42hclgpgfggpxmts9", output: []string{"6", "9"}},
		{input: "fourfourthreehnbhkmscqxdfksg64bvpppznkh", output: []string{"4", "4"}},
	}

	for i, tt := range tests {
		t.Run(fmt.Sprint(i), func(t *testing.T) {
			output := parseStringPart2(tt.input)
			if !reflect.DeepEqual(tt.output, output) {
				t.Errorf("not equal: expected: %+v actual: %+v", tt.output, output)
			}
		})
	}
}
