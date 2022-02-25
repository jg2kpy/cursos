package main

import "fmt"

func main9() {
	slice := []int{1, 2, 3, 4, 5, 6}
	copia := make([]int, len(slice), cap(slice)*2)

	copy(copia, slice) //Copia el minimo de elementos en aamboa arreglos

	fmt.Println(slice)
	fmt.Println(copia)
}
