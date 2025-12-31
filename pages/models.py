from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Subscribers"
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return f"{self.name} ({self.email})"


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Photo"


#notice ko model
from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(
        upload_to='notices/',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('news', 'News'),
        ('classic', 'Classic Text'),
        ('update', 'Update'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


