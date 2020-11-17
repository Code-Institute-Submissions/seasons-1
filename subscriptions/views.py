from django.shortcuts import render, get_object_or_404
from .models import Subscriptions, Size


def subscriptions(request):
    """ A view to the subscriptions page  """
            
    subscriptions = Subscriptions.objects.all()
    context = {
        'subscriptions': subscriptions,
    }

    return render(request, "subscriptions/subscriptions.html", context)


def subscription_detail(request, subscriptions_id):
    """ A view to the selected  subscription """

    size = Size.objects.all()
    subscriptions = get_object_or_404(Subscriptions, pk=subscriptions_id)
    context = {
        'subscriptions': subscriptions,
         'size': size
    }

    return render(request, "subscriptions/subscription_detail.html", context)


def size(request, subscriptions_id):
    """ A view to the selected  subscription """

    size = Size.objects.all()
    context = {
        'size': size,
    }

    return render(request, "subscriptions/subscription_detail.html", context)

