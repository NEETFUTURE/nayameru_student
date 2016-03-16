from django.shortcuts import render, HttpResponse, render_to_response
from django.template import Context, loader
from django.core.context_processors import csrf
import amazonAPI

# Create your views here.
def test(request):
    return render(request, "index.html", {})

def index(request):
    return HttpResponse("This is an index page.")

def find_book(request):
    payload = {}
    payload.update(csrf(request))
    myapi = amazonAPI("AK", "SK", "AT")
    w = request.POST['search_word']
    myapi.search(w)
    books_data = [(myapi.get_with_number(number=(2*i-2)),
                   myapi.get_with_number(number=(2*i-1))) for i in range(1,6)]
    print(books_data)
    payload.update({"books_data":books_data})
    return render_to_response("index.html",
                              payload)