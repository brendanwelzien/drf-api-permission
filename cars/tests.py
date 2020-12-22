from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Car

class CarModelTest(TestCase):

    def test_content(self):
        car = Car.objects.get(id=1)

        self.assertEqual(str(car.name), 'Supra')
        self.assertEqual(car.year, '1999')
        self.assertEqual(car.make, 'Toyota')