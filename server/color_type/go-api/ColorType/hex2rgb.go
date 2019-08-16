package main

import (
	"fmt"
	"regexp"
	"strings"
)

const (
	hexRegexString = "^(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"
	hexFormat      = "%02x%02x%02x"
	hexShortFormat = "%1x%1x%1x"
	hexToRGBFactor = 16
)

var (
	hexRegex = regexp.MustCompile(hexRegexString)
)

// ParseHEX validates and parses the provided string into a ColorHEX object
func ParseHEX(s string) (*ColorHEX, error) {

	s = strings.ToLower(s)

	if !hexRegex.MatchString(s) {
		return nil, fmt.Errorf("Bad HEX color format %s", s)
	}

	return &ColorHEX{Hexcode: s}, nil
}

// HEX2RGB converts the color from HEX to RGB representation
func HEX2RGB(col *ColorHEX) *ColorRGB {

	var r, g, b uint8

	if len(col.Hexcode) == 4 {
		fmt.Sscanf(col.Hexcode, hexShortFormat, &r, &g, &b)
		r *= hexToRGBFactor
		g *= hexToRGBFactor
		b *= hexToRGBFactor
	} else {
		fmt.Sscanf(col.Hexcode, hexFormat, &r, &g, &b)
	}

	return &ColorRGB{R: r, G: g, B: b}
}
