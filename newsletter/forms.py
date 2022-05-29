"""[forms newsletter]"""
from django import forms
from .models import NewsletterUser
# pylint: disable=no-member


class NewsletterUserSignUpForm(forms.ModelForm):
    """[forms newsletter]"""
    class Meta:
        """[metaforms newsletter]"""
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            """[clean email]"""
            email = self.cleaned_data.get('email')

            return email
