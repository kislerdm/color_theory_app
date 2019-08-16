package main

// ColorRGB RGB color code
type ColorRGB struct {
	R uint8 `json:"r"`
	G uint8 `json:"g"`
	B uint8 `json:"b"`
}

// ColorHEX HEX color code
type ColorHEX struct {
	Hexcode string `json:"hexcode"`
}

// Data output JSON
type Data struct {
	Color  ColorRGB `json:"color"`
	IsWarm uint8    `json:"is_warm"`
}

// Response final response JSON
type Response struct {
	Data Data `json:"data"`
}
