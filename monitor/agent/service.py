from .collector import collect_metrics
from .sender import send_metrics
from time import sleep

def run_agent(url: str, interval: int):
    while True:
        metric = collect_metrics()
        send_metrics(metric, url)
        sleep(interval)

def run_agent_locally(interval: int):
    while True:
        metric = collect_metrics()
        print(metric)
        sleep(interval)

# run_agent_locally(5)
