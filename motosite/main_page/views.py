from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Motorcycle

# Create your views here.
def index(request):
    motorcycles = Motorcycle.objects.all()
    data = {
        'title': 'Мотосайт',
        'motorcycles': motorcycles,
    }
    return render(request, 'main_page/index.html', data)

def handler404(request, exception):
    return HttpResponseNotFound(f"<h1>404: {exception}</h1>")