from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer


class ManufacturerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            email="",
            password="password",
            license_number="GF43212",
        )

        self.manufacturer1 = Manufacturer.objects.create(
            name="Toyota",
            country=""
        )

        self.manufacturer2 = Manufacturer.objects.create(
            name="Tesla",
            country=""
        )

    def test_search_manufacturer(self):
        self.client.force_login(self.user)

        url = reverse("taxi:manufacturer-list")
        response = self.client.get(url, {"name": "Toy"})

        self.assertContains(response, "Toyota")
        self.assertNotContains(response, "Tesla")

        self.assertEqual(response.status_code, 200)
