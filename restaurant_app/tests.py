from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Menu, Booking


class AuthAndCRUDTests(APITestCase):
    def setUp(self):
        # cria usuário para autenticação
        self.username = "tester"
        self.password = "secret123!"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        # cria um item de menu para testes
        self.menu = Menu.objects.create(
            name="Pizza",
            description="Cheese Pizza",
            price=25.50
        )

        # cria um booking para testes
        self.booking = Booking.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="123456789",
            date="2025-09-01",
            time="19:00",
            guests=2
        )

    def test_login_and_get_token(self):
        url = reverse("token_obtain_pair")  # precisa estar no urls.py
        response = self.client.post(url, {
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.token = response.data["access"]

    def test_menu_crud(self):
        # autentica
        self.test_login_and_get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # CREATE
        url = reverse("menu-list")
        response = self.client.post(url, {
            "name": "Burger",
            "description": "Beef Burger",
            "price": "18.90"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # READ
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

        # UPDATE
        menu_id = response.data[0]["id"]
        url_detail = reverse("menu-detail", args=[menu_id])
        response = self.client.put(url_detail, {
            "name": "Burger Updated",
            "description": "Delicious beef burger",
            "price": "20.00"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # DELETE
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_booking_crud(self):
        # autentica
        self.test_login_and_get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # CREATE
        url = reverse("booking-list")
        response = self.client.post(url, {
            "name": "Alice",
            "email": "alice@example.com",
            "phone": "987654321",
            "date": "2025-09-02",
            "time": "20:30",
            "guests": 4
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # READ
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
