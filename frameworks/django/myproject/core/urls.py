from django.urls import path
from .views import hello


# URL config
urlpatterns = [
    path('hello/', hello)
]
