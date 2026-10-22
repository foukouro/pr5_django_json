from models import Appointment, Specialist


def test_specialist_creation_and_string_representation() -> None:
    specialist = Specialist(1, "Анна Иванова", "КПТ", 5)

    assert specialist.id == 1
    assert specialist.name == "Анна Иванова"
    assert str(specialist) == "Анна Иванова (КПТ, опыт 5 лет)"


def test_specialist_experience_threshold() -> None:
    specialist = Specialist(1, "Анна Иванова", "КПТ", 5)

    assert specialist.is_experienced()
    assert specialist.is_experienced(5)
    assert not specialist.is_experienced(6)


def test_appointment_links_specialist_and_can_be_cancelled() -> None:
    specialist = Specialist(2, "Петр Сидоров", "Гештальт-терапия", 8)
    appointment = Appointment(7, specialist, "Иван", "2026-11-01")

    assert appointment.specialist is specialist
    assert appointment.status == "Ожидает"
    assert str(appointment) == (
        "Запись №7: Иван к Петр Сидоров на 2026-11-01 (Ожидает)"
    )

    appointment.cancel()

    assert appointment.status == "Отменена"
