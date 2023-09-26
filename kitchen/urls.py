from django.contrib import admin
from django.urls import path

from kitchen.views import index

urlpatterns = [
    path("", index, name="hello"),
]

app_name = "kitchen"