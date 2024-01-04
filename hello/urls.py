# web_project/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    # ...
    path('hello/<str:name>/', views.hello_there, name='hello_there'),
    path('kontakt/', views.kontakt, name='kontakt'),
    # ...
]



