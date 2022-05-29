"""[views for stor aplication]"""
from django.shortcuts import render
# pylint: disable=unused-argument


def handler400(request, exception):
    """[Handler for Bad Request 400]"""
    return render(request, "400.html", status=400)


def handler403(request, exception):
    """[Handler forbidden request 403]"""
    return render(request, "403.html", status=403)


def handler404(request, exception):
    """[Handler for not found request 404]"""
    return render(request, "404.html", status=404)


def handler500(request, *args, **argv):
    """[Handler for internal server error generic message 500]"""
    return render(request, "500.html", status=500)
