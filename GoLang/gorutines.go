package main

import (
	"fmt"
	"strings"
	"time"
)

func main14() {
	go mi_nombre_lentooo("Junior")
	fmt.Println("Que aburridooo")
	var wait string
	fmt.Scanln(&wait)
}

func mi_nombre_lentooo(name string) {
	letras := strings.Split(name, "")

	for _, letra := range letras {
		time.Sleep(1000 * time.Millisecond)
		fmt.Println(letra)
	}
}
