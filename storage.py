import json
from pathlib import Path
from typing import List

from models import Appointment, Specialist


DATA_DIR = Path(__file__).resolve().parent / "data"


def _data_path(path: str | Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return DATA_DIR.parent / candidate


def load_specialists(
    path: str | Path = "data/specialists.json",
) -> List[Specialist]:
    """Load specialist records from JSON as domain objects."""
    with _data_path(path).open(encoding="utf-8") as data_file:
        data = json.load(data_file)
    return [
        Specialist(
            specialist_id=item["id"],
            name=item["name"],
            specialization=item["specialization"],
            experience_years=item["experience_years"],
        )
        for item in data
    ]


def save_specialists(
    specialists: List[Specialist],
    path: str | Path = "data/specialists.json",
) -> None:
    """Save specialist objects as JSON-compatible dictionaries."""
    records = [
        {
            "id": specialist.id,
            "name": specialist.name,
            "specialization": specialist.specialization,
            "experience_years": specialist.experience_years,
        }
        for specialist in specialists
    ]
    destination = _data_path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as data_file:
        json.dump(records, data_file, ensure_ascii=False, indent=2)


def load_appointments(
    specialists: List[Specialist],
    path: str | Path = "data/appointments.json",
) -> List[Appointment]:
    """Load appointments and resolve specialist IDs to objects."""
    with _data_path(path).open(encoding="utf-8") as data_file:
        data = json.load(data_file)
    specialists_by_id = {item.id: item for item in specialists}
    appointments = []
    for item in data:
        specialist = specialists_by_id.get(item["specialist_id"])
        if specialist is None:
            continue
        appointments.append(
            Appointment(
                appointment_id=item["id"],
                specialist=specialist,
                client_name=item["client_name"],
                date=item["date"],
                status=item.get("status", "Ожидает"),
            )
        )
    return appointments


def save_appointments(
    appointments: List[Appointment],
    path: str | Path = "data/appointments.json",
) -> None:
    """Save appointments using specialist IDs instead of object copies."""
    records = [
        {
            "id": appointment.id,
            "specialist_id": appointment.specialist.id,
            "client_name": appointment.client_name,
            "date": appointment.date,
            "status": appointment.status,
        }
        for appointment in appointments
    ]
    destination = _data_path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as data_file:
        json.dump(records, data_file, ensure_ascii=False, indent=2)
