from django import forms
from .models import Feedback

class FeedbackSubmission(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'user_name',
            'user_info',
            'image',
            'stars',
        )