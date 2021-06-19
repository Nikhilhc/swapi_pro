from rest_framework import serializers
from .models import Resource

class student_serializers(serializers.ModelSerializer):
    class Meta:
        model= Resource
        fields = '__all__'