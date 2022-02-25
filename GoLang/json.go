package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Curso struct {
	Title        string
	NumeroVideos int
}

type Cursos []Curso

func main121() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		cursos := Cursos{
			Curso{"Curso de Go", 30},
			Curso{"Curso de Go", 40},
			Curso{"Curso de Go", 50},
		}
		json.NewEncoder(w).Encode(cursos)
	})
	http.ListenAndServe(":8000", nil)
	fmt.Println("Hola mundo")
}
