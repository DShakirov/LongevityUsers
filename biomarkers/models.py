from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from .diseases import SEX

User = get_user_model()


class Diabetes(models.Model):

    result = models.BooleanField(null=True, verbose_name="Result")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="diabetes", null=True, blank=True)
    glucose_level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(150)],
        blank=True,
        null=True,
        verbose_name="Glucose level",
    )
    blood_pressure_diastolic = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(150)],
        blank=True,
        null=True,
        verbose_name="Blood pressure diastolic",
    )
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(110)],
        blank=True,
        null=True,
        verbose_name="Age",
    )
    bmi = models.FloatField(
        null=True,
        blank=True,
        default=None,
        verbose_name="BMI",
        help_text=None,
    )

    def __str__(self):
        return "Diabetes({}) for user: {}".format(self.id, self.user)


class Stroke(models.Model):

    result = models.BooleanField(null=True, verbose_name="Result")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="stroke", null=True, blank=True,)
    glucose_level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(150)],
        blank=True,
        null=True,
        verbose_name="Glucose level",
    )
    bmi = models.FloatField(
        null=True,
        blank=True,
        default=None,
        verbose_name="BMI",
        help_text=None,
    )
    blood_pressure_systolic = models.PositiveIntegerField(
        validators=[MinValueValidator(70), MaxValueValidator(300)],
        blank=True,
        null=True,
        verbose_name="Blood pressure systolic",
    )
    blood_pressure_diastolic = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(150)],
        blank=True,
        null=True,
        verbose_name="Blood pressure diastolic",
    )
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(110)],
        blank=True,
        null=True,
        verbose_name="Age",
    )

    def __str__(self):
        return "Stroke({}) for user: {}".format(self.id, self.user.username)


class LungCancer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="lung_cancer", null=True, blank=True
    )
    result = models.BooleanField(null=True, verbose_name="Result")
    sex = models.CharField(
        max_length=255,
        choices=SEX,
        blank=True,
        null=True,
        verbose_name="Sex",
    )
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(110)],
        blank=True,
        null=True,
        verbose_name="Age",
    )
    smoker = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Smoker",
    )
    yellow_fingers = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Yellow fingers",
    )

    anxiety = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Anxiety",
    )

    peer_pressure = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Peer pressure",
    )

    chronic_disease = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Chronic disease",
    )

    fatigue = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Fatigue",
    )
    allergy = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Allergy",
    )
    wheezing = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Wheezing",
    )
    alcohol_consumption = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Alcohol Consumption",
    )
    coughing = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Coughing",
    )

    shortness_of_breath = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Shortness of breath",
    )
    hepatitis = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Hepatitis",
    )
    chronic_fatigue = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Chronic fatigue",
    )

    swallowing_difficulty = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Swallowing difficulty",
    )

    chest_pain = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Chest pain",
    )

    def __str__(self):
        return "Lung Cancer({}) for user: {}".format(self.id, self.user)


class Malaria(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Malaria", null=True, blank=True)
    result = models.BooleanField(null=True, verbose_name="Result")
    image = models.ImageField(upload_to="diseases/malaria")

    def __str__(self):
        return "Malaria({}) for user: {}".format(self.id, self.user)


class HeartFailure(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="hearth_failure", null=True, blank=True
    )
    result = models.BooleanField(null=True, verbose_name="Result")
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(110)],
        blank=True,
        null=True,
        verbose_name="Age",
    )
    sex = models.CharField(
        max_length=255,
        choices=SEX,
        blank=True,
        null=True,
        verbose_name="Sex",
    )
    cp = models.IntegerField(verbose_name="Chest pain type", blank=True)
    trestbps = models.IntegerField(verbose_name=" Resting blood pressure", blank=True)
    chol = models.IntegerField(verbose_name="Cholesterol", blank=True)
    fbs = models.IntegerField(verbose_name=" Fasting blood sugar", blank=True)
    restecg = models.IntegerField(verbose_name="Resting ECG", blank=True)
    thalach = models.IntegerField(verbose_name="Max heart rate", blank=True)
    exang = models.BooleanField(verbose_name="Exercise induced angina", blank=True)
    oldpeak = models.FloatField(verbose_name="ST depression", blank=True)
    slope = models.IntegerField(verbose_name=" Slope of peak exercise ST segment", blank=True)
    ca = models.IntegerField(verbose_name="Number of major vessels colored by flourosopy", blank=True)
    thal = models.IntegerField(verbose_name="Thalassemia", blank=True)

    def __str__(self):
        return "Hearth failure({}) for user: {}".format(self.id, self.user)


class CVD(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cvd", null=True, blank=True
    )
    result = models.BooleanField(null=True, verbose_name="Result")
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(110)],
        blank=True,
        null=True,
        verbose_name="Age",
    )
    height = models.FloatField(validators=[MinValueValidator(0.99), MaxValueValidator(2.3)]),
    blood_pressure_sys = models.PositiveIntegerField(
        validators=[MinValueValidator(70), MaxValueValidator(300)],
        blank=True,
        null=True,
        verbose_name="Blood pressure systolic",
    )
    blood_pressure_dia = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(150)],
        blank=True,
        null=True,
        verbose_name="Blood pressure diastolic",
    )
    cholesterol_level = models.IntegerField(
        verbose_name="Cholesterol level",
        blank=True,
        null=True
    )

    def __str__(self):
        return "CVD({}) for user: {}".format(self.id, self.user)


class HIV(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="hiv", null=True, blank=True
    )
    result = models.BooleanField(null=True, verbose_name="Result")

    hiv_diagnosis = models.IntegerField(
                    blank=True,
                    null=True,
                    verbose_name="HIV diagnoses"
    )
    hiv_diagnosis_rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="HIV diagnosis rate"
    )
    concurrent_diagnosis = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Concurrent diagnoses"
    )
    patients_treatment_3_months = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="% linked to care within 3 months"
    )
    aids_diagnosis_rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="AIDS diagnosis rate"
    )
    plwdhi_prevalence = models.FloatField(
        blank=True,
        null=True,
        verbose_name="PLWDHI prevalence"
    )
    viral_suppression = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="% viral suppression"
    )
    deaths = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Deaths"
    )
    death_rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Death rate"
    )
    hiv_death_rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="HIV-related death rate"
    )
    non_hiv_death_rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Non-HIV-related death rate"
    )

    def __str__(self):
        return "HIV({}) for user: {}".format(self.id, self.user)


class COPD(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="copd", null=True, blank=True
    )
    result = models.BooleanField(null=True, verbose_name="Result")
    AGE = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="age"
    )
    PackHistory = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="PackHistory"
    )
    MWT1 = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="1 minute walk test"
    )
    MWT2 = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="2 minute walk test"
    )
    FEV1 = models.FloatField(
        blank=True,
        null=True,
        verbose_name="forced expiratory volume in 1 second"
    )
    FVC = models.FloatField(
        blank=True,
        null=True,
        verbose_name="forced vital capacity"
    )
    CAT = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="COPD Assessment Test"
    )
    HAD = models.IntegerField(
        blank=True,
        null=True,
    )
    SGRQ = models.FloatField(
        blank=True,
        null=True,
        verbose_name="St George's Respiratory Questionnaire"
    )
    copd = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="COPD"
    )
    gender = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="gender"
    )
    smoking = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Smoker"
    )

    def __str__(self):
        return "COPD({}) for user: {}".format(self.id, self.user)


class Leukemia(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Leukemia", null=True, blank=True)
    result = models.BooleanField(null=True, verbose_name="Result")
    image = models.ImageField(upload_to="diseases/leukemia")

    def __str__(self):
        return "Malaria({}) for user: {}".format(self.id, self.user)


class Pneumonia(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pneumonia", null=True, blank=True)
    result = models.BooleanField(null=True, verbose_name="Result")
    image = models.ImageField(upload_to="diseases/pneumonia")

    def __str__(self):
        return "Malaria({}) for user: {}".format(self.id, self.user)


class Melanoma(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="melanoma", null=True, blank=True)
    result = models.BooleanField(null=True, verbose_name="Result")
    image = models.ImageField(upload_to="diseases/malanoma")

    def __str__(self):
        return "Malaria({}) for user: {}".format(self.id, self.user)




