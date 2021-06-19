from rest_framework import viewsets
from . import models
from . import serializers

class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.student_serializers


