package main

import "fmt"

func main7() {
	arreglo := [10]int{1, 2}

	fmt.Println(len(arreglo))

	for i := 0; i < len(arreglo); i = i + 1 {
		fmt.Println(arreglo[i])
	}

	var matrix [2][2]int

	fmt.Println(matrix)
}
