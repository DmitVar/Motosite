from django.shortcuts import render

# Create your views here.
def add_bike(request):
    return render(request,'addbike/addbike.html')