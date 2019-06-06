from django.http import HttpResponse


def index(request):
    return HttpResponse("HOLA RETAMAR. ESTO ES EL INDEX DE MI WEB APP")
