from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'title': 'Мотосайт'}
    return render(request, 'main_page/index.html', data)

def handler404(request, exception):
    return HttpResponseNotFound(f"<h1>404: {exception}</h1>")