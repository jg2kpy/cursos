package main

import (
	"fmt"
	"strconv"
)

func main3() {
	edad := "22"
	edad_int, _ := strconv.Atoi(edad)
	fmt.Println(edad_int + 10)
}
