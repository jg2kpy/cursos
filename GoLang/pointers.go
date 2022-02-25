package main

import "fmt"

func main10() {
	var x, y *int
	entero := 5

	x = &entero
	y = &entero

	*x = 6

	fmt.Println(*x)
	fmt.Println(*y)
}
