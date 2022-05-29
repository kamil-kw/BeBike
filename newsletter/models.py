"""[newsletter models]"""
from django.db import models
# pylint: disable=invalid-str-returned


class NewsletterUser(models.Model):
    """[newsletter user model]"""
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """[newsletter user model]"""
        return self.email
