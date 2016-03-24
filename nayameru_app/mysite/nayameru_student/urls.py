from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^find_book$', views.find_book, name='find_book'),
    url(r"^$", views.test, name="test"),
    url(r'^$', views.index, name='index'),
    url(r"^index$", views.index, name="indx"),
    url(r"^top$", views.top, name="top")
]
