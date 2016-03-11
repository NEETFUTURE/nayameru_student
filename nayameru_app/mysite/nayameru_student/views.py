from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def top(request):
    return render(request, "top.html", {})
