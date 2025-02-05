from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def porto_details(request):
    return render(request, 'portfolio-details.html')