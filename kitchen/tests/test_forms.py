from django.contrib.auth import get_user_model
from django.test import TestCase
from kitchen.forms import CookCreationForm, DishCreateForm


class FormsTest(TestCase):
    def test_cook_creation_form_valid(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
            "years_of_experience": 5,
            "first_name": "John",
            "last_name": "Doe",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class CookCreationFormTest(TestCase):
    def test_valid_years_of_experience(self):
        form = CookCreationForm({
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 10,
        })
        self.assertTrue(form.is_valid())

    def test_negative_years_of_experience(self):
        form = CookCreationForm({
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': -5,
        })
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Years of experience cannot be negative.',
            form.errors['years_of_experience']
        )

    def test_excessive_years_of_experience(self):
        form = CookCreationForm({
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 60,
        })
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Years of experience cannot be greater than 55 years',
            form.errors['years_of_experience']
        )


class DishCreateFormTest(TestCase):
    def setUp(self):
        self.cook1 = get_user_model().objects.create_user(
            username="cook1",
            password="testpass1"
        )
        self.cook2 = get_user_model().objects.create_user(
            username="cook2",
            password="testpass2"
        )

    def test_negative_price(self):
        form = DishCreateForm({
            'name': 'Spaghetti Bolognese',
            'description': 'Classic Italian pasta with meat sauce',
            'price': -5,
            'dish_type': 1,
            'cooks': [self.cook1.id],
        })
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Price cannot be negative.',
            form.errors['price']
        )

    def test_excessive_price(self):
        form = DishCreateForm({
            'name': 'Spaghetti Bolognese',
            'description': 'Classic Italian pasta with meat sauce',
            'price': 110.00,
            'dish_type': 1,
            'cooks': [self.cook1.id],
        })
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Price cannot be greater than 100.00.',
            form.errors['price']
        )

    def test_missing_cooks(self):
        form = DishCreateForm({
            'name': 'Spaghetti Bolognese',
            'description': 'Classic Italian pasta with meat sauce',
            'price': 10.99,
            'dish_type': 1,
            'cooks': [],
        })
        self.assertFalse(form.is_valid())
        self.assertIn(
            'This field is required.',
            form.errors['cooks']
        )
