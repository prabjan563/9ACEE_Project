from django import forms
from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True
            })
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if email exists and is active
        if Subscriber.objects.filter(email=email, is_active=True).exists():
            # If they're already subscribed, don't error - just let them through
            return email
        return email