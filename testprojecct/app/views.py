from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.serializers import StudentSerializer
from app.models import Student


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
