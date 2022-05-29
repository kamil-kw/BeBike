"""[models for contact app]"""
from django.db import models
# pylint: disable=invalid-str-returned


class Contact(models.Model):
    """[models for contact app]"""
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
