from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from models.specialists import find_specialist_by_id
from storage import load_specialists


def specialist_list(request: HttpRequest) -> HttpResponse:
    """Render the available specialists."""
    context = {"specialists": load_specialists()}
    return render(request, "specialists/specialist_list.html", context)


def specialist_detail(
    request: HttpRequest,
    specialist_id: int,
) -> HttpResponse:
    """Render a specialist detail or a not-found state."""
    specialist = find_specialist_by_id(load_specialists(), specialist_id)
    context = {"specialist": specialist}
    status = 404 if specialist is None else 200
    return render(
        request,
        "specialists/specialist_detail.html",
        context,
        status=status,
    )
