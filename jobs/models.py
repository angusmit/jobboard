from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('jobseeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)  # For employers
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # For job seekers

    class Meta:
        app_label = 'jobs'  # Add this line

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()  # For employer contact
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    employer = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
        null=True,  # Allow null temporarily
        blank=True   # Allow blank in forms
    )

    def __str__(self):
        return f"{self.title} at {self.company}"