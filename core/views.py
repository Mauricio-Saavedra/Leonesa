from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mision(request):
    return render(request, 'mision.html')

def visit(request):
    return render(request, 'visit.html')

def historia(request):
    return render(request, 'historia.html')

def other(request):
    return render(request, 'other.html')