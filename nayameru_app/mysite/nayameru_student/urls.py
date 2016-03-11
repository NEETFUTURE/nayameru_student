from django.conf.urls import url
from .import views

urlpatterns = [
    url(r"^index$", views.index, name="indx"),
    url(r"^top$", views.top, name="top")
]
