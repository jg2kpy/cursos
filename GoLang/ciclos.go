package main

import "fmt"

func main6() {
	for i := 0; i < 10; i = i + 1 {
		fmt.Println("hello world")
	}
	i := 0
	for i < 10 {
		fmt.Println(i)
		i++
	}
	for {
		fmt.Println(i) //infinito
		i++
	}
}
