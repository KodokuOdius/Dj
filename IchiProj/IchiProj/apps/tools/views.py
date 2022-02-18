from aiohttp import request
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
