from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import(
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


class DiabetesSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)

    class Meta:
        model = Diabetes
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        diabetes_list = Diabetes.objects.filter(user=user)
        if diabetes_list.exists():
            raise ValidationError('Diabetes data already exists')
        return super().create(validated_data)


class StrokeSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)

    class Meta:
        model = Stroke
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        stroke_list = Stroke.objects.filter(user=user)
        if stroke_list.exists():
            raise ValidationError('Stroke data already exists')
        return super().create(validated_data)


class LungCancerSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)

    class Meta:
        model = LungCancer
        fields = "__all__"


    def create(self, validated_data):
        user = validated_data['user']
        Lung_cancer_list = LungCancer.objects.filter(user=user)
        if Lung_cancer_list.exists():
            raise ValidationError('Lung cancer data already exists')
        return super().create(validated_data)


class MalariaSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)
    image = Base64ImageField()

    class Meta:
        model = Malaria
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        malaria_list = Malaria.objects.filter(user=user)
        if malaria_list.exists():
            raise ValidationError('Malaria data already exists')
        return super().create(validated_data)


class HeartFailureSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)

    class Meta:
        model = HeartFailure
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        heart_failure_list = HeartFailure.objects.filter(user=user)
        if heart_failure_list.exists():
            raise ValidationError('Heart failure data already exists')
        return super().create(validated_data)


class CVDSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)

    class Meta:
        model = CVD
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        cvd_list = CVD.objects.filter(user=user)
        if cvd_list.exists():
            raise ValidationError('CVD data already exists')
        return super().create(validated_data)


class HIVSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)

    class Meta:
        model = HIV
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        hiv_list = HIV.objects.filter(user=user)
        if hiv_list.exists():
            raise ValidationError('HIV data already exists')
        return super().create(validated_data)


class COPDSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)

    class Meta:
        model = COPD
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        copd_list = COPD.objects.filter(user=user)
        if copd_list.exists():
            raise ValidationError('COPD data already exists')
        return super().create(validated_data)


class LeukemiaSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)
    image = Base64ImageField()

    class Meta:
        model = Leukemia
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        leukemia_list = Leukemia.objects.filter(user=user)
        if leukemia_list.exists():
            raise ValidationError('Leukemia data already exists')
        return super().create(validated_data)


class PneumoniaSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)
    image = Base64ImageField()

    class Meta:
        model = Pneumonia
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        pneumonia_list = Pneumonia.objects.filter(user=user)
        if pneumonia_list.exists():
            raise ValidationError('Pneumonia data already exists')
        return super().create(validated_data)


class MelanomaSerializer(serializers.ModelSerializer):

    result = serializers.BooleanField(required=False)
    image = Base64ImageField()

    class Meta:
        model = Melanoma
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user']
        melanoma_list = Melanoma.objects.filter(user=user)
        if melanoma_list.exists():
            raise ValidationError('Melanoma data already exists')
        return super().create(validated_data)