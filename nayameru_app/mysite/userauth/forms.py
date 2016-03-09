from django import forms
from.models import CustomUser
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password", "universityname", "email")
        widgets = {
            "username" : forms.TextInput(attrs={"size" : 40}),
            "password" : forms.PasswordInput(attrs={"size" : 40}),
            "universityname" : forms.TextInput(attrs={"size" : 40}),
            #"email" : forms.EmailField(),
            "email" : forms.EmailInput()
        }


    def clean_username(self):
        username = self.cleaned_data["username"]

        return username


    def clean_password(self):
        password = self.cleaned_data["password"]

        return password


    def clean_universityname(self):
        name = self.cleaned_data["universityname"]

        return name


    def clean_email(self):
        email = self.cleaned_data["email"]

        return email


class loginForm(forms.Form):
    username = forms.CharField(
        label="ユーザ名",
        required=True
    )

    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput()
    )