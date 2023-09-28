from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    num_of_cook = Cook.objects.count()
    num_of_dish = Dish.objects.count()
    num_of_dish_type = DishType.objects.count()
    context = {
        "num_of_cook": num_of_cook,
        "num_of_dish": num_of_dish,
        "num_of_dish_type": num_of_dish_type
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishListView(generic.ListView):
    model = Dish
