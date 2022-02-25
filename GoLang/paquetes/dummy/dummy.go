package dummy

var hola_mundo string

func init() {
	hola_mundo = "hola mundo"
}

func HolaMundo() string {
	return hola_mundo
}

func holaMundoDos() string {
	return "No me puedes ejecutar"
}
