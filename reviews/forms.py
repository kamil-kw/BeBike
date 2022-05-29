"""[forms reviews]"""
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """[Form to add reviews of products]"""
    class Meta:
        """[Form meta]"""
        model = Review
        fields = ('description',)
