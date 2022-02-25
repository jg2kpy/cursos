package main

import (
	"bufio"
	"fmt"
	"os"
)

func main4() {
	precio := 14.2
	fmt.Printf("Mi edad es %f\n", precio)

	var edad int
	fmt.Println("Coloca a tu edad: ")
	fmt.Scanf("%d\n", &edad)
	fmt.Printf("Mi edad es %d\n", edad)

	reader := bufio.NewReader(os.Stdin)
	text, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Hola " + text)
	}
}
