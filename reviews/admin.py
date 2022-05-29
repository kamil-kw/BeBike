"""[admin reviews]"""
from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """[admin reviews]"""
    list_display = (
        'product',
        'user',
        'review_date'
    )
