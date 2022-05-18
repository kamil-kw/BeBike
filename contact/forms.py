from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Form for Contact model that uses all fields
    """
    class Meta:
        model = Contact
        fields = '__all__'