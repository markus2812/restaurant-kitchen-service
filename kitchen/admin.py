from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Dish, DishType, Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "years_of_experience", "is_staff")
    list_filter = ("years_of_experience", )
    search_fields = ("username", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("years_of_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("first_name", "last_name",
                                                                               "years_of_experience",)}),)

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

