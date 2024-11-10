from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

@csrf_exempt
def home(requests):
    # print( dir(requests))
    if requests.method == "GET":
        html = '<!DOCTYPE html> <html lang="es"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Formulario de Ejemplo</title> </head> <body> <h1>Formulario de Contacto</h1> <form action="http://127.0.0.1:8000/" method="POST"> <label for="nombre">Nombre:</label> <input type="text" id="nombre" name="nombre" required><br><br> <label for="email">Correo Electrónico:</label> <input type="email" id="email" name="email" required><br><br> <label for="mensaje">Mensaje:</label><br> <textarea id="mensaje" name="mensaje" rows="4" cols="50" required></textarea><br><br> <input type="submit" value="Enviar"> </form> </body> </html>'
        return HttpResponse(html)
    elif requests.method == "POST":
        print(requests.POST)
        html = '<html lang="en"><body>GRacias por completar el fomrulario!</body></html>'
        return HttpResponse(html)
    


def productos(requests):
    if requests.method == "GET":
        data = [
            {
                "id": "1",
                "title": "reloj xiomi",
                "precio": 122,
                "stock": True
            },
            {
                "id": "2",
                "title": "reloj xiomi 2",
                "precio": 44,
                "stock": True
            },
        ]
        
        return JsonResponse(data, safe=False)
