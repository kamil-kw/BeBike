"""[Views newsletter]"""
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm
# pylint: disable=no-member


def newsletter_subscribe(request):
    """ A view to return the index page """

    return render(request, 'newsletter/newsletter_subscription.html')


def newsletter_signup(request):
    """[newsletter_signup]"""
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,
                             'Sorry, this email is already \
                                 subscribed to our newsletter!')
        else:
            messages.success(request,
                             'Your email is been added \
                                 succesfully to receive our newsletter!')
            instance.save()
            subject = "Thank you for Joining our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = """Welcome to BeBike Newsletter, \
                If you would like to unsubscribe visit \
                    https://bebike.herokuapp.com/newsletter/unsubscribe/"""
            send_mail(subject=subject,
                      from_email=from_email,
                      recipient_list=to_email,
                      message=signup_message,
                      fail_silently=False)

    context = {
        'form': form,
    }

    template = 'newsletter/signup.html'

    return render(request, template, context)


def newsletter_unsubscribe(request):
    """[newsletter unsubscribe]"""
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                             'Your email is \
                                 removed from our database')
        else:
            messages.warning(request,
                             'Sorry but your email \
                                 did not exist in our database')

    context = {
        'form': form,
    }

    template = 'newsletter/unsubscribe.html'

    return render(request, template, context)
