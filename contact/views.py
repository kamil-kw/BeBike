from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your mail was send !!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'There Was an Error Trying to Send Email Message,\
                    Please check your form.'
            )
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)