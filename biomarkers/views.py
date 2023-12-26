from django.contrib.auth import get_user_model
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


from .models import (
    Diabetes,
    Stroke,
    LungCancer,
    Malaria,
    HeartFailure,
    CVD,
    HIV,
    COPD,
    Leukemia,
    Pneumonia,
    Melanoma
)
from .serializers import (
    DiabetesSerializer,
    StrokeSerializer,
    LungCancerSerializer,
    MalariaSerializer,
    HeartFailureSerializer,
    CVDSerializer,
    HIVSerializer,
    COPDSerializer,
    LeukemiaSerializer,
    PneumoniaSerializer,
    MelanomaSerializer
)

from users.permissions import IsOwnerOrIsDoctor

User = get_user_model()


class CreateDiabetesView(generics.CreateAPIView):
    """
    Request for creating diabetes data
    Use POST method
    Structure of request:
    {
        "result": true,
        "glucose_level": 150,
        "blood_pressure_diastolic": 150,
        "age": 110,
        "bmi": 0,
        "user": "string"
    }
    """
    queryset = Diabetes.objects.all()
    serializer_class = DiabetesSerializer
    permission_classes = (IsAuthenticated,)


class UpdateDiabetesView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete diabetes data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = Diabetes.objects.all()
    serializer_class = DiabetesSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        diabetes_instance = get_object_or_404(Diabetes, user=user)
        return diabetes_instance


class CreateStrokeView(generics.CreateAPIView):
    """
    Request for creating stroke data
    Use POST method
    Structure of request:
        {
          "result": true,
          "glucose_level": 150,
          "bmi": 0,
          "blood_pressure_systolic": 300,
          "blood_pressure_diastolic": 150,
          "age": 110,
          "user": "string"
        }
    """
    queryset = Stroke.objects.all()
    serializer_class = StrokeSerializer
    permission_classes = (IsAuthenticated,)


class UpdateStrokeView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete stroke data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = Stroke.objects.all()
    serializer_class = StrokeSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        stroke_instance = get_object_or_404(Stroke, user=user)
        return stroke_instance


class CreateLungCancerView(generics.CreateAPIView):
    """
    Request for creating lung cancer data
    Use POST method
    Structure of request:
        {
          "result": true,
          "sex": "MALE",
          "age": 110,
          "smoker": true,
          "yellow_fingers": true,
          "anxiety": true,
          "peer_pressure": true,
          "chronic_disease": true,
          "fatigue": true,
          "allergy": true,
          "wheezing": true,
          "alcohol_consumption": true,
          "coughing": true,
          "shortness_of_breath": true,
          "hepatitis": true,
          "chronic_fatigue": true,
          "swallowing_difficulty": true,
          "chest_pain": true,
          "user": "string"
        }
    """
    queryset = LungCancer.objects.all()
    serializer_class = LungCancerSerializer
    permission_classes = (IsAuthenticated,)


class UpdateLungCancerView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete lung cancer data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = LungCancer.objects.all()
    serializer_class = LungCancerSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        lung_cancer_instance = get_object_or_404(LungCancer, user=user)
        return lung_cancer_instance


class CreateMalariaView(generics.CreateAPIView):
    """
     Request for creating malaria data
     Use POST method
     Structure of request:
        {
          "result": true,
          "user": "string",
          "image": image.jpg
        }
     """
    queryset = Malaria.objects.all()
    serializer_class = MalariaSerializer
    permission_classes = (IsAuthenticated,)


class UpdateMalariaView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete malaria data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = Malaria.objects.all()
    serializer_class = MalariaSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        malaria_instance = get_object_or_404(Malaria, user=user)
        return malaria_instance


class CreateHeartFailureView(generics.CreateAPIView):
    """
     Request for creating heart  data
     Use POST method
     Structure of request:
        {
          "result": true,
          "age": 110,
          "sex": "MALE",
          "cp": 2147483647,
          "trestbps": 2147483647,
          "chol": 2147483647,
          "fbs": 2147483647,
          "restecg": 2147483647,
          "thalach": 2147483647,
          "exang": true,
          "oldpeak": 0,
          "slope": 2147483647,
          "ca": 2147483647,
          "thal": 2147483647,
          "user": "string"
        }
     """
    queryset = HeartFailure.objects.all()
    serializer_class = HeartFailureSerializer
    permission_classes = (IsAuthenticated,)


class UpdateHeartFailureView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete heart failure data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = HeartFailure.objects.all()
    serializer_class = HeartFailureSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        heart_failure_instance = get_object_or_404(HeartFailure, user=user)
        return heart_failure_instance


class CreateCVDView(generics.CreateAPIView):
    """
     Request for creating CVD data
     Use POST method
     Structure of request:
        {
          "result": true,
          "age": 110,
          "blood_pressure_sys": 300,
          "blood_pressure_dia": 150,
          "cholesterol_level": 2147483647,
          "user": "string"
        }
     """
    queryset = CVD.objects.all()
    serializer_class = CVDSerializer
    permission_classes = (IsAuthenticated,)


class UpdateCVDView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete CVD data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = CVD.objects.all()
    serializer_class = CVDSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        cvd_instance = get_object_or_404(CVD, user=user)
        return cvd_instance


class CreateHIVView(generics.CreateAPIView):
    """
     Request for creating HIV data
     Use POST method
     Structure of request:
        {
          "result": true,
          "hiv_diagnosis": 2147483647,
          "hiv_diagnosis_rate": 0,
          "concurrent_diagnosis": 2147483647,
          "patients_treatment_3_months": 2147483647,
          "aids_diagnosis_rate": 0,
          "plwdhi_prevalence": 0,
          "viral_suppression": 2147483647,
          "deaths": 2147483647,
          "death_rate": 0,
          "hiv_death_rate": 0,
          "non_hiv_death_rate": 0,
          "user": "string"
        }
     """
    queryset = HIV.objects.all()
    serializer_class = HIVSerializer
    permission_classes = (IsAuthenticated,)


class UpdateHIVView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete HIV data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = HIV.objects.all()
    serializer_class = HIVSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        hiv_instance = get_object_or_404(HIV, user=user)
        return hiv_instance


class CreateCOPDView(generics.CreateAPIView):
    """
     Request for creating COPD data
     Use POST method
     Structure of request:
        {
          "result": true,
          "AGE": 2147483647,
          "PackHistory": true,
          "MWT1": 2147483647,
          "MWT2": 2147483647,
          "FEV1": 0,
          "FVC": 0,
          "CAT": 2147483647,
          "HAD": 2147483647,
          "SGRQ": 0,
          "copd": true,
          "gender": 2147483647,
          "smoking": true,
          "user": "string"
        }
    """
    queryset = COPD.objects.all()
    serializer_class = COPDSerializer
    permission_classes = (IsAuthenticated,)


class UpdateCOPDView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete COPD data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = COPD.objects.all()
    serializer_class = COPDSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        copd_instance = get_object_or_404(COPD, user=user)
        return copd_instance


class CreateLeukemiaView(generics.CreateAPIView):
    """
     Request for creating leukemia data
     Use POST method
     Structure of request:
        {
          "result": true,
          "user": "string",
          "image": image.jpg
        }
     """
    queryset = Leukemia.objects.all()
    serializer_class = LeukemiaSerializer
    permission_classes = (IsAuthenticated,)


class UpdateLeukemiaView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete leukemia data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = Leukemia.objects.all()
    serializer_class = LeukemiaSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        leukemia_instance = get_object_or_404(Leukemia, user=user)
        return leukemia_instance


class CreatePneumoniaView(generics.CreateAPIView):
    """
     Request for creating pneumonia data
     Use POST method
     Structure of request:
        {
          "result": true,
          "user": "string",
          "image": image.jpg
        }
     """
    queryset = Pneumonia.objects.all()
    serializer_class = PneumoniaSerializer
    permission_classes = (IsAuthenticated,)


class UpdatePneumoniaView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete pneumonia data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = Pneumonia.objects.all()
    serializer_class = PneumoniaSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        pneumonia_instance = get_object_or_404(Pneumonia, user=user)
        return pneumonia_instance


class CreateMelanomaView(generics.CreateAPIView):
    """
     Request for creating leukemia data
     Use POST method
     Structure of request:
        {
          "result": true,
          "user": "string",
          "image": image.jpg
        }
     """
    queryset = Melanoma.objects.all()
    serializer_class = MelanomaSerializer
    permission_classes = (IsAuthenticated,)


class UpdateMelanomaView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to fetch, update or delete melanoma data
    Use GET method to fetch data, PUT/PATCH method to update data and DELETE method to delete data
    """
    queryset = Melanoma.objects.all()
    serializer_class = MelanomaSerializer
    permission_classes = (IsOwnerOrIsDoctor,)

    def get_object(self):
        cognito_username = self.kwargs['cognito_username']
        user = get_object_or_404(User, cognito_username=cognito_username)
        melanoma_instance = get_object_or_404(Melanoma, user=user)
        return melanoma_instance