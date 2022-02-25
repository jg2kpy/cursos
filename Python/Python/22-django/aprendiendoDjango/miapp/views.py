from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
    <h1>Sitio Web con Django</h1>
    <hr/
    <ul>
        <li>
            <a href="/">Inicio<a>
        </li>

        <li>
            <a href="/hola-mundo">Hola Mundo<a>
        </li>

        <li>
            <a href="/pagina-pruebas">Pagina de pruebas<a>
        </li>

        <li>
            <a href="/contacto-dos">Contacto<a>
        </li>
    </ul>
"""


def index(request):

    """

    html = ""
        <h1>Incio</h1>
        <p> Ano pares antes del 2050:</p>
        <ul>
    ""

    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"

    """

    year = 2021

    hasta = range(year, 2051)

    nombre = "Junior Gutierrez"

    lenguajes = ['JavaScript','Python','PHP','C']

    return render(request,"index.html", {
        'title': 'Inicio 2',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):
    return render(request,"hola_mundo.html")


def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect("contacto", nombre="Junior",apellidos="Gutierrez")

    return render(request,"pagina.html",{
        'texto': "Este es mi texto",
        'lista': ['uno','dos','tres']
    })


def contacto(request, nombre="", apellidos=""):
    html = ""
    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>Contacto {nombre} {apellidos}<h3>"
    return HttpResponse(layout + f"<h2>Contacto {nombre} {apellidos}<h2>"+html)
