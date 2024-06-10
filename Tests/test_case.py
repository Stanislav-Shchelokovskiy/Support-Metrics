from typing import Protocol
from server_models import TicketsWithIterationsParams


class TestCase(Protocol):
    group_by: str
    start: str
    end: str
    baseline_aligned_mode_enabled: bool
    metric: str
    body: TicketsWithIterationsParams
