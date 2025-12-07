from django.db import models
from django.contrib.auth.models import User

# Existing PaperSubmission model
class PaperSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author_fullname = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    author_list = models.TextField()
    presenting_author = models.CharField(max_length=200)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_fullname} - {self.user.username}"


# ✅ Add this new model for Photos
class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Photo {self.id}"

