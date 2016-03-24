from django.shortcuts import render, HttpResponse, render_to_response
from django.template import Context, loader
from django.core.context_processors import csrf
#import amazonAPI
from .amazonAPI import amazonAPI
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from .models import SearchLog


#@login_required #ログイン必須にするデコレータ
def test(request):
    return render(request, "index.html", {})


def index(request):
    return HttpResponse("This is an index page.")


#@login_required #ログイン必須にするデコレータ
@require_GET
def find_book(request):
    #教科書名1,教科書名2,教科書名3,... みたいな感じの複数教科書名検索に対応させる必要あり…？

    payload = {}
    payload.update(csrf(request))
    myapi = amazonAPI("AK", "SK", "AT")
    w = request.GET['search_word']
    myapi.search(w)
    books_data = [(myapi.get_with_number(number=(2*i-2)),
                   myapi.get_with_number(number=(2*i-1))) for i in range(1,6)]
    print(books_data)
    payload.update({"books_data":books_data})

    #検索ログの保存
    # new_log = SearchLog(
    #     user_id=request.user.id,
    #     book_name=w,
    #     lowest_price=0
    # )
    # new_log.save()

    return render_to_response("index.html",
                              payload)


#viewのコントローラ内部でのみ利用可能
#自分と同じ大学のユーザの検索履歴を取ってくる
# def osusume(req):
#     universityname = req.user.universityname
#     logs = SearchLog.objects.filter(user__universityname=universityname)
#     tmp = [log.book_name for log in logs]
#
#     return tmp
# Create your views here.
def index(request):
    return render(request, "index.html", {})

def top(request):
    return render(request, "top.html", {})
