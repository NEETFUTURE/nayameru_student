from django.shortcuts import (
    render,
    redirect
)
from .models import CustomUser
from .forms import (
    UserForm,
    loginForm
)
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def touroku(request):
    form = UserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            universityname = request.POST["universityname"]
            email = request.POST["email"]

            new_user = CustomUser(
                username = username,
                universityname=universityname,
                email=email
            )
            new_user.set_password(password)
            new_user.save()

            messages.success(request, "登録が完了しました")
            #return redirect("nayameru_student:index") #ここ変更されるかもね
            return redirect("userauth:touroku")
        else:
            messages.error(request, "何かしらのミスがあるよぉ") #あかりちゃん

    d = {
        "form" : form,
        "users" : CustomUser.objects.all()
    }

    return render(request, "userauth/touroku.html", d) #ファイル名はまだ未定


def login(request):
    form = loginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth_login(request, user)

                    #どっかからログインページに強制リダイレクトされた場合は元の場所に飛ばす
                    if request.GET.get("next"):
                        return redirect(request.GET["next"])

            else:
                messages.error(request, "ログインに失敗しました")

    d = {
        "form" : form
    }

    return render(request, "userauth/loginpage.html", d) #ファイル名はまだ未定


def logout(request):
    auth_logout(request)
    messages.success(request, "ログアウトに成功しました")
    #return redirect("nayameru_student:index") #ここ変更されるかもね
    return redirect("userauth:touroku")


@login_required
def testlogin(request):
    return HttpResponse("ここはログインが必要なページです")
