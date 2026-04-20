import psutil
from datetime import datetime
from .models import Metric

def collect_metrics() -> Metric:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timestamp = datetime.now()
    
    return Metric(cpu=cpu, memory=memory, disk=disk, timestamp=timestamp)
