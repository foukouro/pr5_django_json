from typing import List, Optional


class Specialist:
    """Therapist or counselor available through the service."""

    def __init__(
        self,
        specialist_id: int,
        name: str,
        specialization: str,
        experience_years: int,
    ) -> None:
        self.id = specialist_id
        self.name = name
        self.specialization = specialization
        self.experience_years = experience_years

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.specialization}, "
            f"опыт {self.experience_years} лет)"
        )

    def is_experienced(self, min_years: int = 3) -> bool:
        return self.experience_years >= min_years


def find_specialist_by_id(
    specialists: List[Specialist],
    specialist_id: int,
) -> Optional[Specialist]:
    """Return the specialist with the requested ID, if present."""
    return next(
        (item for item in specialists if item.id == specialist_id),
        None,
    )
