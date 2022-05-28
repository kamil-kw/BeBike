from django.shortcuts import render
from django.contrib import messages

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

def newsletter_subscribe(request):
    """ A view to return the index page """

    return render(request, 'newsletter/newsletter_subscription.html')


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Sorry, this email is already subscribed to our newsletter!')
            # messages.info(request, 'Sorry, this email is already subscribed to our newsletter!')
        else:
            messages.success(request, 'Your email is been added succesfully to receive our newsletter!')
            instance.save()

    context = {
        'form': form,
    }

    template = 'newsletter/signup.html'

    return render(request, template, context)

def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your email is removed from our database')
        else:
            messages.warning(request, 'Sorry but your email did not exist in our database')

    context = {
        'form': form,
    }

    template = 'newsletter/unsubscribe.html'

    return render(request, template, context)