package main

import (
	"bufio"
	"fmt"
	"os"
)

func main17() {
	fmt.Println(read_file())
	recover()
	fmt.Println("hola")
}

func read_file() bool {
	archivo, err := os.Open("./hola1.txt")
	defer func() {
		archivo.Close()
		recover()
	}()

	if err != nil {
		//fmt.Println(err)
		panic(err)
	}

	scanner := bufio.NewScanner(archivo)

	for scanner.Scan() {
		linea := scanner.Text()

		fmt.Println(linea)
	}
	return true
}
