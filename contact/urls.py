from django.urls import path

# - - - - - Internal imports - - - - - - - - -
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
]