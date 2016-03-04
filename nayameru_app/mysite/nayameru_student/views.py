from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, "index.html", {})

def index(request):
    return HttpResponse("This is an index page.")
