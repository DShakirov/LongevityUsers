from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

User = get_user_model()


class UserViewTest(APITestCase):

    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username="shakirovdominatus@gmail.com",
            defaults={
                "email": "shakirovdominatus@gmail.com",
                "is_doctor": True,
                "is_staff": True,
            }
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_fetch_success(self):
        response = self.client.get(
            reverse('users:user', kwargs={'pk': self.user.pk})
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetch_error_not_owner(self):
        self.user.is_doctor = False
        print(self.user.is_doctor)
        user, created = User.objects.get_or_create(
            username="test@test.com",
            defaults={
                "email": "test@test.com",
            }
        )

        response = self.client.get(
            reverse('users:user', kwargs={'pk': user.pk})
            )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_success(self):
        user, created = User.objects.get_or_create(
            username="test@test.com",
            defaults={
                "email": "test@test.com",
            }
            )

        response = self.client.delete(
            reverse('users:delete', kwargs={'pk': user.pk})
            )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_error_is_not_staff(self):
        self.user.is_staff = False
        user, created = User.objects.get_or_create(
            username="test@test.com",
            defaults={
                "email": "test@test.com",
            }
            )

        response = self.client.delete(
            reverse('users:delete', kwargs={'pk': user.pk})
            )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
