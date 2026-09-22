from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['opiniao']
        labels = {
            'opiniao': 'Sua opinião',
        }
        widgets = {
            'opiniao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite aqui sua opinião sobre o sistema...',
                    'rows': 6,
                }
            ),
        }
