from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class DriverSearchTest(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="tj_test",
            email="",
            password="password",
            license_number="ADC54321",
        )

        self.user2 = get_user_model().objects.create_user(
            username="oj_test",
            email="",
            password="password123",
            license_number="ADC12345",
        )

        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="",
            password="password",
            license_number="ADC21312",
        )

    def test_driver_search(self):
        self.client.force_login(self.admin_user)

        url = reverse("taxi:driver-list")
        response = self.client.get(url, {"username": "tj_test"})

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "tj_test")
        self.assertNotContains(response, "oj_test")

        drivers = response.context["driver_list"]
        self.assertIn(self.user1, drivers)
        self.assertNotIn(self.user2, drivers)
        self.assertNotIn(self.admin_user, drivers)
