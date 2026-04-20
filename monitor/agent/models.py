from dataclasses import dataclass
from datetime import datetime

@dataclass
class Metric:
    cpu: float
    memory: float
    disk: float
    timestamp: datetime
