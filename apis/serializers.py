from rest_framework import serializers
from .models import Message, Students, News, Quotas, Vacancys, Images


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class QuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotas
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancys
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
