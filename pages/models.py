from django.db import models
import re

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

class FVideo(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField(help_text="Enter YouTube video URL")
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def get_youtube_id(self):
        """Extract YouTube video ID from various URL formats"""
        if not self.youtube_url:
            return ''
        
        # Pattern for different YouTube URL formats
        patterns = [
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})',
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
            r'(?:https?:\/\/)?youtu\.be\/([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.youtube_url)
            if match:
                return match.group(1)
        
        return ''
    
    def get_youtube_embed_url(self):
        """Convert YouTube URL to embed URL"""
        video_id = self.get_youtube_id()
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return ''
    
    def get_thumbnail_url(self):
        """Get YouTube thumbnail URL"""
        video_id = self.get_youtube_id()
        if video_id:
            return f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
        return ''
    

class Speaker(models.Model):
    SPEAKER_TYPES = [
        ('keynote', 'Keynote Speaker'),
        ('invited', 'Invited Speaker'),
    ]
    
    speaker_type = models.CharField(max_length=10, choices=SPEAKER_TYPES)
    name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='speakers/')
    
    # For Keynote Speakers
    talk_title = models.CharField(max_length=500, blank=True, null=True, help_text="For keynote speakers")
    abstract = models.TextField(blank=True, null=True, help_text="For keynote speakers")
    
    # For Invited Speakers
    session = models.CharField(max_length=300, blank=True, null=True, help_text="For invited speakers")
    
    # Common fields
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.get_speaker_type_display()}"
    



class Venue(models.Model):
    title = models.CharField(max_length=200, default="Venue")
    description = models.TextField(blank=True)
    location = models.CharField(max_length=300, blank=True)
    details = models.TextField(blank=True, help_text="Additional venue details (TBA)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Venue"
        verbose_name_plural = "Venues"

    def __str__(self):
        return self.title


class FieldVisit(models.Model):
    title = models.CharField(max_length=200, default="Field Visit")
    location = models.CharField(max_length=300, default="Bhaktapur")
    description = models.TextField(blank=True)
    logistics = models.TextField(blank=True, help_text="Logistics details (TBA)")
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Field Visit"
        verbose_name_plural = "Field Visits"

    def __str__(self):
        return f"{self.title} - {self.location}"


class Accommodation(models.Model):
    title = models.CharField(max_length=200, default="Accommodation")
    description = models.TextField(blank=True)
    hotel_partners = models.TextField(blank=True, help_text="List of hotel partners")
    booking_guidance = models.TextField(blank=True, help_text="Booking instructions (TBA)")
    website_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Accommodation"
        verbose_name_plural = "Accommodations"

    def __str__(self):
        return self.title


class Travel(models.Model):
    title = models.CharField(max_length=200, default="Travel & Visa")
    travel_guidance = models.TextField(blank=True, help_text="General travel guidance (TBA)")
    visa_notes = models.TextField(blank=True, help_text="Visa information and requirements")
    local_transportation = models.TextField(blank=True, help_text="Local transportation details (TBA)")
    airport_info = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Travel Information"
        verbose_name_plural = "Travel Information"

    def __str__(self):
        return self.title
    
class Popup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='popup_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Only one popup will be shown at a time")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Popup"
        verbose_name_plural = "Popups"
    
    def __str__(self):
        return self.title


