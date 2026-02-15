from dataclasses import dataclass
from typing import Protocol


@dataclass
class AssessmentAttempt:
    student_id: str
    module_id: str
    answers: dict[str, str]
    attempt_count: int


@dataclass
class AssessmentResult:
    student_id: str
    module_id: str
    score_percent: float
    passed: bool


class AssessmentService(Protocol):
    def evaluate(self, attempt: AssessmentAttempt) -> AssessmentResult:
        """Score completion test using question bank and governance rules."""
