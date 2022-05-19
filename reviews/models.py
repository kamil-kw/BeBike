from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """[Review model]"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=False,
                                   blank=False)
    review_date = models.DateTimeField(auto_now_add=True)