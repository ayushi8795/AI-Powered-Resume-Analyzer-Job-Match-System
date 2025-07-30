from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ResumeSerializer, JobDescriptionSerializer
from .models import Resume, JobDescription
from .utils import extract_text_from_resume
from .nlp_parser import parse_resume
import os

# Create your views here.
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def perform_create(self,serializer):
        instance = serializer.save()
        file_path = instance.resume_file.path
        try:
            text = extract_text_from_resume(file_path)
            paresed = parse_resume(text)
            instance.parsed_skills = paresed['skills']
            instance.parsed_education = paresed['education']    
            instance.parsed_experience = paresed['experience']
            instance.save()
        except Exception as e:
            print(f"Error parsing resume: {e}")
class JobDescriptionViewSet(viewsets.ModelViewSet):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
