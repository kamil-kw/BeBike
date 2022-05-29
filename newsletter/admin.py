"""[admin newsleter]"""
from django.contrib import admin

# Register your models here.
from .models import NewsletterUser


class NewsletterAdmin(admin.ModelAdmin):
    """[admin newsleter]"""
    list_display = ('email', 'date_added',)


admin.site.register(NewsletterUser, NewsletterAdmin)
