package main

import (
	"fmt"
	"io/ioutil"
)

func main16() {
	file_data, err := ioutil.ReadFile("./hola.txt")

	if err != nil {
		fmt.Println("ERROR")
	}

	fmt.Println(string(file_data))
}
