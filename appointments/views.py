from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from models.appointments import find_appointment_by_id
from storage import load_appointments, load_specialists


def appointment_list(request: HttpRequest) -> HttpResponse:
    """Render the appointments and their statuses."""
    specialists = load_specialists()
    appointments = load_appointments(specialists)
    context = {"appointments": appointments}
    return render(request, "appointments/appointment_list.html", context)


def appointment_detail(
    request: HttpRequest,
    appointment_id: int,
) -> HttpResponse:
    """Render an appointment detail or a not-found state."""
    specialists = load_specialists()
    appointments = load_appointments(specialists)
    appointment = find_appointment_by_id(appointments, appointment_id)
    context = {"appointment": appointment}
    status = 404 if appointment is None else 200
    return render(
        request,
        "appointments/appointment_detail.html",
        context,
        status=status,
    )
