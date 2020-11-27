from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("booking", views.booking, name="booking"),
    path("book", views.book, name="book")
]

