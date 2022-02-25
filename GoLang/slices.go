package main

import "fmt"

func main8() {
	slices := []int{1, 2, 3, 4} //esto es un slice
	fmt.Println(len(slices))

	arreglo := [3]int{1, 2, 3}

	slices2 := arreglo[:] //slicing
	fmt.Println(slices2)
}
