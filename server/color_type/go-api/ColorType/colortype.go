package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
)

// Model function to predict the color type
func Model(col *ColorRGB) uint8 {

	if col.R > col.G &&
		col.G > col.B {
		return 1
	}
	return 0
}

func byRGB(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Server", "dkisler.com")
	w.Header().Set("Content-Type", "application/json")

	RequestQuery := r.URL.Query()
	R, err := strconv.Atoi(RequestQuery["r"][0])
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(`{"data": null}`))
		e := fmt.Sprintf("Red from query %s cannot be parsed", RequestQuery)
		log.Print(e)
		return
	}

	G, err := strconv.Atoi(RequestQuery["g"][0])
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(`{"data": null}`))
		e := fmt.Sprintf("Green from query %s cannot be parsed", RequestQuery)
		log.Print(e)
		return
	}

	B, err := strconv.Atoi(RequestQuery["b"][0])
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(`{"data": null}`))
		e := fmt.Sprintf("Blue from query %s cannot be parsed", RequestQuery)
		log.Print(e)
		return
	}

	color := &ColorRGB{
		R: uint8(R),
		G: uint8(G),
		B: uint8(B),
	}

	dat := Response{
		Data: Data{
			Color:  *color,
			IsWarm: Model(color),
		},
	}

	resp, err := json.Marshal(dat)

	if err != nil {
		w.Write([]byte(`{"data": null}`))
		w.WriteHeader(http.StatusInternalServerError)
		e := fmt.Sprintf("Cannot parse %b as JSON", dat)
		log.Print(e)
	} else {
		w.WriteHeader(http.StatusOK)
		w.Write(resp)
	}
}

func byHEX(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Server", "dkisler.com")
	w.Header().Set("Content-Type", "application/json")

	RequestQuery := r.URL.Query()["hexcode"][0]
	colorhex, err := ParseHEX(RequestQuery)

	if err != nil {
		e := fmt.Sprintf("Wrong input format HEX code '%s' cannot be parsed\n", RequestQuery)
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(`{"data": null}`))
		log.Print(e)
	} else {
		color := HEX2RGB(colorhex)

		dat := Response{
			Data: Data{
				Color:  *color,
				IsWarm: Model(color),
			},
		}

		resp, err := json.Marshal(dat)
		if err != nil {
			e := fmt.Sprintf("Cannot parse %b as JSON", dat)
			w.WriteHeader(http.StatusInternalServerError)
			w.Write([]byte(`{"data": null}`))
			log.Print(e)
		} else {
			w.WriteHeader(http.StatusOK)
			w.Write(resp)
		}
	}
}

func main() {
	var PORT = 4501
	http.HandleFunc("/rgb", byRGB)
	http.HandleFunc("/hex", byHEX)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", PORT), nil))
}
