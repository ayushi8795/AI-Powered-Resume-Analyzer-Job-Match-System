from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ResumeSerializer, JobDescriptionSerializer
from .models import Resume, JobDescription

# Create your views here.
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class JobDescriptionViewSet(viewsets.ModelViewSet):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
