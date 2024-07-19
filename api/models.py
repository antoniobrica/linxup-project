from django.db import models

class UserProfile(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField()
    linkedin = models.URLField(blank=True, null=True)
    branch = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    satisfaction = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    skills = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
