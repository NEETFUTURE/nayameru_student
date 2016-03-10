from django.shortcuts import render, HttpResponse, render_to_response
from django.template import Context, loader
import amazonAPI

# Create your views here.
def test(request):
    return render(request, "index.html", {})

def index(request):
    return HttpResponse("This is an index page.")

def find_book(request,q):
    myapi = amazonAPI("AK", "SK", "AT")
    myapi.search(q["word"])
    books_data = [myapi.get_with_number(number=i) for i in range(1,11)]

    return render_to_response("index.html",
                              {"books_data":books_data})
