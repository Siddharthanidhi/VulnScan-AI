from dataclasses import dataclass, field
from datetime import datetime
import requests


@dataclass
class ScanContext:

    target: str

    session: requests.Session

    response: requests.Response | None = None

    started_at: datetime = field(
        default_factory=datetime.utcnow
    )

    metadata: dict = field(
        default_factory=dict
    )

    collector_results: dict = field(
        default_factory=dict
    )

    evidence_package: dict = field(
        default_factory=dict
    )

    observations: list = field(
        default_factory=list
    )