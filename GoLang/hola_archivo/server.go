package main

import "net/http"

func main() {
	fileServer := http.FileServer(http.Dir("public"))
	http.Handle("/public/", http.StripPrefix("/public/", fileServer))
	http.ListenAndServe(":8000", nil)
}
