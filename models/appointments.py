from typing import List, Optional

from .specialists import Specialist


class Appointment:
    """Appointment between a client and a specialist."""

    def __init__(
        self,
        appointment_id: int,
        specialist: Specialist,
        client_name: str,
        date: str,
        status: str = "Ожидает",
    ) -> None:
        self.id = appointment_id
        self.specialist = specialist
        self.client_name = client_name
        self.date = date
        self.status = status

    def __str__(self) -> str:
        return (
            f"Запись №{self.id}: {self.client_name} к "
            f"{self.specialist.name} на {self.date} ({self.status})"
        )

    def cancel(self) -> None:
        self.status = "Отменена"


def find_appointment_by_id(
    appointments: List[Appointment],
    appointment_id: int,
) -> Optional[Appointment]:
    """Return the appointment with the requested ID, if present."""
    return next(
        (item for item in appointments if item.id == appointment_id),
        None,
    )
