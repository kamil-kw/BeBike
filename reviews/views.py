from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm

from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    """
    Add a product review
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            Review.objects.create(user=user, product=get_object_or_404(Product,
                                  pk=product_id), description=description)
            messages.success(request, 'You review has been \
                successfully added.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Please try again.')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """
    Edit a product review
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'You review has been \
            successfully edited.')
            return redirect(
                reverse('product_detail', args=(review.product.id,)))
        else:
            messages.error(request, 'Please try again.')
    else:
        form = ReviewForm(instance=review)

    template = "reviews/edit_review.html"
    context = {
        "form": form,
        "review": review,
        "product": review.product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Delete a product review
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=(review.product.id,)))
