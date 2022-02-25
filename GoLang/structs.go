package main

import "fmt"

type User struct {
	edad             int
	nombre, apellido string
}

func (this User) nombre_completo() string {
	return this.nombre + " " + this.apellido
}

func main11() {
	junior := User{20, "Junior", "Gutierrez"}
	fmt.Println(junior.nombre_completo())
}
