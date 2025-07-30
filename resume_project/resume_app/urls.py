from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResumeViewSet, JobDescriptionViewSet

router = DefaultRouter()
router.register(r'resumes', ResumeViewSet)
router.register(r'jobDescriptions',JobDescriptionViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
