from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Cook, Dish

DISHT_TYPE_URL = reverse("kitchen:dish-type-list")
DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISHT_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.cook = get_user_model().objects.create_user(
            username="testusername",
            first_name="testfirstname",
            last_name="testlastname",
            password="testpass"
        )
        self.client.force_login(self.cook)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="test1")
        DishType.objects.create(name="test2")
        response = self.client.get(DISHT_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(list(response.context["dish_type_list"]), list(dish_types))
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")


class PublicCookTest(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testusername",
            first_name="testfirstname",
            last_name="testlastname",
            password="testpass"
        )
        self.client.force_login(self.user)
        self.cook = Cook.objects.create(username="user1",
                                        years_of_experience=3
                                        )
        self.cook = Cook.objects.create(username="another_user",
                                        years_of_experience=3
                                        )

        self.cook = Cook.objects.create(username="test1",
                                        first_name="test1",
                                        last_name="test1",
                                        years_of_experience=8
                                        )
        self.cook = Cook.objects.create(username="test3",
                                        first_name="test3",
                                        last_name="test3",
                                        years_of_experience=15
                                        )

    def test_retrieve_cook(self):
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all()
        self.assertEqual(list(response.context["cook_list"]),
                         list(cooks)
                         )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_cook_search_with_results(self):
        url = reverse("kitchen:cook-list") + "?username=user1"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "user1")
        self.assertNotContains(response, "user2")

    def test_search_with_no_results(self):
        url = reverse("kitchen:cook-list") + "?username=nonexistent_user"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "user1")
        self.assertNotContains(response, "user2")
        self.assertNotContains(response, "another_user")


class PublicDishTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testusername",
            first_name="testfirstname",
            last_name="testlastname",
            password="testpass"
        )
        self.client.force_login(self.user)
        dishtype = DishType.objects.create(
            name="test"
        )
        self.dish1 = Dish.objects.create(
            name="test_name",
            description="test123",
            price=4,
            dish_type=dishtype,
        )
        self.dish2 = Dish.objects.create(
            name="test_name2",
            description="5",
            price=5,
            dish_type=dishtype,
        )
        self.dish3 = Dish.objects.create(
            name="test_name3",
            description="test1234",
            price=6,
            dish_type=dishtype,
        )

    def test_retrieve_dish(self):
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish_list"]),
                         list(dishes)
                         )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_dish_search_with_results(self):
        url = reverse("kitchen:dish-list") + "?name=test_name"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test_name")
        self.assertNotContains(response, "another_test_name")

    def test_search_with_no_results(self):
        url = reverse("kitchen:dish-list") + "?name=nonexistent_dish"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "test_name")
        self.assertNotContains(response, "another_test_name")
        self.assertNotContains(response, "another_dish")