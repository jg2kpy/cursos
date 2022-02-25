package main

import "fmt"

type Human struct {
	name string
}

type Tutor struct {
	Human
}

func main12() {
	tutor := Tutor{Human{"Junior"}}

	fmt.Println(tutor.name)
}
