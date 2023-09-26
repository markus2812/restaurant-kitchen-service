from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    num_of_cook = Cook.objects.count()
    num_of_dish = Dish.objects.count()
    num_of_dish_type = DishType.objects.count()
    return HttpResponse(f"<h1>Hello Mate!</h1>"
                        f"<ul>"
                        f"<li>Num of cook: {num_of_cook}</li>"
                        f"<li>Num of dish: {num_of_dish}</li>"
                        f"<li>Num of dish-type: {num_of_dish_type}</li>"
                        f"</ul>")

