import random


def generate_common_metrics():
    return {
        "cpu_usage": round(random.uniform(10, 60), 2),
        "memory_usage": round(random.uniform(20, 70), 2),
        "response_time": round(random.uniform(0.1, 1.0), 3),
        "availability": round(random.uniform(0.95, 1.0), 3),
        "cost": round(random.uniform(0.01, 0.5), 4),
        "rtt": round(random.uniform(5, 30), 2),
        "throughput": round(random.uniform(200, 800), 2),
        "latency": round(random.uniform(5, 25), 2),
    }


def scenario_operational():
    metrics = generate_common_metrics()
    metrics["service_type"] = "web"
    return metrics


def scenario_unstable():
    metrics = generate_common_metrics()
    metrics["cpu_usage"] = round(random.uniform(60, 90), 2)
    metrics["memory_usage"] = round(random.uniform(70, 90), 2)
    metrics["response_time"] = round(random.uniform(1.5, 5.0), 3)
    metrics["availability"] = round(random.uniform(0.8, 0.94), 3)
    metrics["latency"] = round(random.uniform(30, 70), 2)
    metrics["rtt"] = round(random.uniform(50, 120), 2)
    metrics["service_type"] = "api"
    return metrics


def scenario_anomalous():
    metrics = {
        "cpu_usage": 0.0,
        "memory_usage": 0.0,
        "response_time": None,
        "availability": 0.0,
        "cost": 0.0,
        "rtt": None,
        "throughput": 0.0,
        "latency": None,
        "service_type": "unknown",
    }
    return metrics
