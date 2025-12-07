from django import forms
from .models import PaperSubmission

class PaperSubmissionForm(forms.ModelForm):
    class Meta:
        model = PaperSubmission
        fields = [
            'author_fullname',
            'affiliation',
            'designation',
            'country',
            'email',
            'phone',
            'author_list',
            'presenting_author'
        ]
