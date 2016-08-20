from django.core.serializers import json
from django.http import HttpResponse


def index(request):
    with open('data.json') as data_file:
        data = json.load(data_file)
    
    return HttpResponse("Hello, world. You're at the index.")
