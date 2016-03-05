from django.conf.urls import url
from .import views

urlpatterns = [
    url(r"^$", views.test, name="test"),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='find_book'),
]
