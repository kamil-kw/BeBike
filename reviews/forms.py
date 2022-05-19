from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """[Form to add reviews of products]"""
    class Meta:
        model = Review
        fields = ('description',)