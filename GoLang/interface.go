package main

import "fmt"

type User2 interface {
	Permisos() int
	Nombre() string
}

type Admin struct {
	nombre string
}

func (this Admin) Permisos() int {
	return 5
}

func (this Admin) Nombre() string {
	return this.nombre
}

func auth(user User2) string {
	if user.Permisos() > 4 {
		return user.Nombre() + " tiene permisos de administrador"
	}
	return ""
}

func main13() {
	admin := Admin{"Junior"}
	fmt.Println(auth(admin))
}
