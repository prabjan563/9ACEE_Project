from django.contrib import admin
from .models import Photo, Notice, Post, Video  , Subscriber , FVideo
from .models import Speaker
from .models import Venue, FieldVisit, Accommodation, Travel
from .models import Popup


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['name', 'email']
    readonly_fields = ['subscribed_at']
    list_per_page = 50

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
    search_fields = ['title']

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'message']
    fields = ['title', 'message', 'image', 'is_active']  # Make sure image is included

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'content']
    fields = ['title', 'content', 'image', 'category']  # Make sure image is included

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(FVideo)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order', 'created_at']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']




@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'speaker_type', 'affiliation', 'is_active', 'order')
    list_filter = ('speaker_type', 'is_active')
    search_fields = ('name', 'affiliation')
    list_editable = ('order', 'is_active')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('speaker_type', 'name', 'affiliation', 'photo', 'is_active', 'order')
        }),
        ('Keynote Speaker Details', {
            'fields': ('talk_title', 'abstract'),
            'description': 'Fill this section only for Keynote Speakers'
        }),
        ('Invited Speaker Details', {
            'fields': ('session',),
            'description': 'Fill this section only for Invited Speakers'
        }),
    )




@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'is_active', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'location', 'description')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'location', 'is_active')
        }),
        ('Details', {
            'fields': ('description', 'details')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(FieldVisit)
class FieldVisitAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'time', 'is_active', 'updated_at')
    list_filter = ('is_active', 'date', 'created_at')
    search_fields = ('title', 'location', 'description')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'location', 'is_active')
        }),
        ('Schedule', {
            'fields': ('date', 'time')
        }),
        ('Details', {
            'fields': ('description', 'logistics')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('title', 'website_url', 'is_active', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description', 'hotel_partners')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'is_active')
        }),
        ('Details', {
            'fields': ('description', 'hotel_partners', 'booking_guidance', 'website_url')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'travel_guidance', 'visa_notes')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'is_active')
        }),
        ('Travel Information', {
            'fields': ('travel_guidance', 'local_transportation', 'airport_info')
        }),
        ('Visa Information', {
            'fields': ('visa_notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Popup)
class PopupAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']



