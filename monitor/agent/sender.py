from .models import Metric
import requests

def send_metrics(metric: Metric, url: str):
    data = {
        'cpu': metric.cpu,
        'memory': metric.memory,
        'disk': metric.disk,
        'timestamp': metric.timestamp.isoformat()
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send metrics: {e}")
