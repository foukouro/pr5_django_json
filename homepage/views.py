from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Render the service landing page."""
    return render(request, "homepage/index.html")


def page_not_found(
    request: HttpRequest,
    exception: Exception,
) -> HttpResponse:
    """Render the shared 404 page."""
    return render(request, "404.html", status=404)
