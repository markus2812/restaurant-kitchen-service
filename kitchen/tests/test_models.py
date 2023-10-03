from django.test import TestCase

from kitchen.models import DishType, Dish, Cook


class ModelTests(TestCase):
    def SetUp(self):
        self.cook = Cook.objects.create(
            username="test",
            years_of_experience=3,
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = Cook.objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(cook), f"{cook.first_name} {cook.last_name} ({cook.username})"
        )

    def test_dish_str(self):
        dishtype = DishType.objects.create(name="test")
        dish = Dish.objects.create(
            name="test_name",
            description="test123",
            price=4,
            dish_type=dishtype,
        )
        self.assertEqual(str(dish), f"{dish.name}{dish.price}")

    def test_cook_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = 3
        cook = Cook.objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
