from dataclasses import dataclass
from typing import Protocol

from src.intake.interfaces import StudentProfile


@dataclass
class LearningGoal:
    goal_id: str
    title: str


@dataclass
class LearningPath:
    student_id: str
    recommended_modules: list[str]
    estimated_total_minutes: int


class RecommendationService(Protocol):
    def recommend(self, profile: StudentProfile, goals: list[LearningGoal]) -> LearningPath:
        """Map goals and profile gaps to a prioritized module path."""
