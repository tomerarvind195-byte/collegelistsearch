from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    about = models.TextField(blank=True)

    # Academic Preferences
    target_exam = models.CharField(max_length=100)
    expected_rank = models.PositiveIntegerField(null=True, blank=True)
    preferred_stream = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    preferred_cities = models.CharField(max_length=300)

    # Profile Statistics (Optional)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    saved_colleges = models.PositiveIntegerField(default=0)
    applications = models.PositiveIntegerField(default=0)
    recommendations = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username