from django.db import models

# Create your models here.
class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to='AppResumes/')
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class JobDescription(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.FileField(upload_to = "AppJobDescriptions/")
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title
