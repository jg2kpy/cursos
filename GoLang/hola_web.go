package main

import (
	"fmt"
	"io"
	"net/http"
)

func main208() {
	http.HandleFunc("/holamundo", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Nueva peticion")
		io.WriteString(w, "Hola mundoooo")
	})
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8000", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Nueva peticion")
	io.WriteString(w, "Hola mundo")
}
