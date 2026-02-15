from dataclasses import dataclass
from typing import Protocol


@dataclass
class IntakeInput:
    student_id: str
    current_level: str
    language_preference: str


@dataclass
class StudentProfile:
    student_id: str
    current_level: str
    language_preference: str


class IntakeService(Protocol):
    def collect_profile(self, payload: IntakeInput) -> StudentProfile:
        """Validate, normalize and return a student profile."""
