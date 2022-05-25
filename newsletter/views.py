from django.shortcuts import render
from django.contrib import messages

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.info(request, 'Sorry, this email is already subscribed to our newsletter!')
        else:
            messages.success(request, 'Your email is been added succesfully to receive our newsletter!')
            instance.save()

    context = {
        'form': form,
    }

    template = 'newsletter/newsletter_signup.html'

    return render(request, template, context)