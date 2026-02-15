from dataclasses import dataclass
from typing import Protocol, Any


@dataclass
class AnalyticsEvent:
    event_id: str
    event_type: str
    student_id: str
    source_package: str
    payload: dict[str, Any]


@dataclass
class MetricSnapshot:
    metric_name: str
    metric_value: float


class AnalyticsService(Protocol):
    def ingest(self, event: AnalyticsEvent) -> None:
        """Collect and validate incoming domain events."""

    def compute_metrics(self) -> list[MetricSnapshot]:
        """Compute rollup metrics from collected events."""
