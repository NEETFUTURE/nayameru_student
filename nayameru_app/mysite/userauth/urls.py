from django.conf.urls import url
from .import views

urlpatterns = [
    url(r"^touroku$", views.touroku, name="touroku"),
]