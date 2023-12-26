import os
import base64

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from ..models import Diabetes

User = get_user_model()


class DiabetesViewTest(APITestCase):

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

    def test_success(self):
        payload = {
            "user": self.user.pk,
            "glucose_level": 10,
            "blood_pressure_diastolic": 90,
            "age": 38,
            "bmi": 22
        }
        response = self.client.post(
            reverse("biomarkers:create_diabetes"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # object sucessfully created
        payload = {
            "result": True,
            "glucose_level": 10,
            "blood_pressure_diastolic": 90,
            "age": 38,
            "bmi": 22
        }
        response = self.client.put(
            reverse("biomarkers:diabetes", kwargs={"cognito_username": self.user.pk}),
            payload, format="json"
        )
        print(response.data, len(Diabetes.objects.all()))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_diabetes_already_exists(self):
        payload = {
            "user": self.user.pk,
            "glucose_level": 10,
            "blood_pressure_diastolic": 90,
            "age": 38,
            "bmi": 22
        }
        response = self.client.post(
            reverse("biomarkers:create_diabetes"), payload, format='json'
        )
        response = self.client.post(
            reverse("biomarkers:create_diabetes"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class StrokeViewTest(APITestCase):

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

    def test_success(self):

        payload = {
            "user": self.user.pk,
            "glucose_level": 10,
            "blood_pressure_diastolic": 90,
            "blood_pressure_systolic": 100,
            "age": 38,
            "bmi": 22
        }
        response = self.client.post(
            reverse("biomarkers:create_stroke"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        payload = {
            "user": self.user.pk,
            "result": True,
            "glucose_level": 10,
            "blood_pressure_diastolic": 149,
            "blood_pressure_systolic": 100,
            "age": 38,
            "bmi": 22
        }
        response = self.client.put(
            reverse("biomarkers:stroke", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LungCancerViewTest(APITestCase):

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

    def test_success(self):
        payload = {
            "user": self.user.pk,
            "age": 38,
            "smoker": False,
            "yellow_fingers": False,
            "anxiety": False,
            "peer_pressure": False,
            "chronic_disease": False,
            "fatigue": False,
            "allergy": False,
            "wheezing": False,
            "alcohol_consumption": False,
            "coughing": False,
            "shortness_of_breath": False,
            "hepatitis": False,
            "chronic_fatigue": False,
            "swallowing_difficulty": False,
            "chest_pain": False,
        }
        response = self.client.post(
            reverse("biomarkers:create_lung_cancer"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        payload = {
            "result": False,
        }
        response = self.client.put(
            reverse("biomarkers:lung_cancer", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MalariaViewTest(APITestCase):
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

    def test_success(self):
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.jpg')
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            encoded_image_data = base64.b64encode(image_data).decode('utf-8')
            payload = {
                "user": self.user.pk,
                "image": encoded_image_data
            }
        response = self.client.post(
            reverse("biomarkers:create_malaria"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #object sucessfully created
        payload = {
            "result": False,
            "user": self.user.pk,
            "image": encoded_image_data
        }
        response = self.client.put(
            reverse("biomarkers:malaria", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HeartFailureViewTest(APITestCase):
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

    def test_success(self):
        payload = {
            "user": self.user.pk,
            "age": 38,
            "sex": "MALE",
            "cp": 1,
            "trestbps": 3,
            "chol": 4,
            "fbs": 5,
            "restecg": 6,
            "thalach": 7,
            "exang": False,
            "oldpeak": 11,
            "slope": 10,
            "ca": 11,
            "thal": 12,
        }
        response = self.client.post(
            reverse("biomarkers:create_heart_failure"), payload, format='json'
            )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #object sucessfully created
        payload = {
            "result": False,
        }
        response = self.client.put(
            reverse("biomarkers:heart_failure", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CVDViewTest(APITestCase):
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

    def test_success(self):
        payload = {
            "user": self.user.pk,
            "age": 38,
            "blood_pressure_sys": 90,
            "blood_pressure_dia": 89,
            "cholesterol_level": 5
        }
        response = self.client.post(
            reverse("biomarkers:create_cvd"), payload, format='json'
            )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #object sucessfully created
        payload = {
            "result": False,
            "user": self.user.pk,
        }
        response = self.client.put(
            reverse("biomarkers:cvd", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class COPDViewTest(APITestCase):
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

    def test_success(self):
        payload = {
            "user": self.user.pk,
            "AGE": 38,
            "PackHistory": False,
            "MWT1": 1,
            "MWT2":2,
            "FEV1": 3,
            "FVC": 4,
            "CAT": 6,
            "HAD": 5,
            "SGRQ": 8,
            "copd": False,
            "gender": 1,
            "smoking": False

        }
        response = self.client.post(
            reverse("biomarkers:create_copd"), payload, format='json'
            )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #object sucessfully created
        payload = {
            "result": False,
            "user": self.user.pk,
        }
        response = self.client.put(
            reverse("biomarkers:copd", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeukemiaViewTest(APITestCase):
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

    def test_success(self):
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.jpg')
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            encoded_image_data = base64.b64encode(image_data).decode('utf-8')
            payload = {
                "user": self.user.pk,
                "image": encoded_image_data
            }
        response = self.client.post(
            reverse("biomarkers:create_leukemia"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #object sucessfully created
        payload = {
            "result": False,
            "user": self.user.pk,
            "image": encoded_image_data
        }
        response = self.client.put(
            reverse("biomarkers:leukemia", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PneumoniaViewTest(APITestCase):
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

    def test_success(self):
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.jpg')
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            encoded_image_data = base64.b64encode(image_data).decode('utf-8')
            payload = {
                "user": self.user.pk,
                "image": encoded_image_data
            }
        response = self.client.post(
            reverse("biomarkers:create_pneumonia"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #object sucessfully created
        payload = {
            "result": False,
            "user": self.user.pk,
            "image": encoded_image_data
        }
        response = self.client.put(
            reverse("biomarkers:pneumonia", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MelanomaViewTest(APITestCase):
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

    def test_success(self):
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.jpg')
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            encoded_image_data = base64.b64encode(image_data).decode('utf-8')
            payload = {
                "user": self.user.pk,
                "image": encoded_image_data
            }
        response = self.client.post(
            reverse("biomarkers:create_melanoma"), payload, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #object sucessfully created
        payload = {
            "result": False,
            "user": self.user.pk,
            "image": encoded_image_data
        }
        response = self.client.put(
            reverse("biomarkers:melanoma", kwargs={"cognito_username": self.user.cognito_username}),
            payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

