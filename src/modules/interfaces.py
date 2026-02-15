from dataclasses import dataclass
from typing import Protocol


@dataclass
class ModuleSession:
    student_id: str
    module_id: str
    checkpoints_passed: list[str]


@dataclass
class ModuleCompletion:
    student_id: str
    module_id: str
    completion_status: str


class ModuleLifecycleService(Protocol):
    def evaluate_completion(self, session: ModuleSession) -> ModuleCompletion:
        """Evaluate mandatory conditions and return completion state."""
