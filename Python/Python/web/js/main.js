/*var nombre = "Junior Gutierrez"
var altura = 180

var concatenar = nombre + " " + altura

//document.write(concatenar)
var datos = document.getElementById("datos")
datos.innerHTML = `
    <h1>${nombre}</h1>
`
if (altura >= 190) {
    datos.innerHTML += `<h1> Eres una persona alta </h1>`
} else {
    datos.innerHTML += `<h1> Eres una persona bajita </h1>`
}

for (var i = 2000; i <= 2020; i++) {
    datos.innerHTML += `<h2>Estamos en el ano ${i}</h2>`
} 
*/

function MuestraMiNombre(nombre, altura) {
    var datos = document.getElementById("datos")
    datos.innerHTML = `
        <h1>${nombre}</h1>
    `
}

MuestraMiNombre("Junior")