from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hhh(request):
    yourtext = request.GET["fulltext"]
    return render(request, 'hhh.html',{"yourtext": yourtext})