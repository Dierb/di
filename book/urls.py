from django.urls import path
from . import views



urlpatterns = [
    path('',views.book, name = 'books')
]