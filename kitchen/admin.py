from django.contrib import admin
from kitchen.models import Dish, DishType, Cook


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "years_of_experience", "is_superuser")
    list_filter = ("years_of_experience", )
    search_fields = ("username", )

    verbose_name = "Cook"
    verbose_name_plural = "Cooks"


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "dish_type")
    list_filter = ("dish_type", )
    search_fields = ("name", )

    verbose_name = "Dish"
    verbose_name_plural = "Dishes"


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )

