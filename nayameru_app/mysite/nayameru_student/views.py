from django.shortcuts import render
from django.template import Context, loader
import amazonAPI

# Create your views here.
def test(request):
    return render(request, "index.html", {})

def index(request):
    return HttpResponse("This is an index page.")

def find_book(request,q):
    books_data={}
    return render_to_response("index.html",
                              {"books_data":books_data})
