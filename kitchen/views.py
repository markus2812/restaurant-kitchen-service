from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Cook, Dish, DishType


@login_required
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 10


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 10


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook

