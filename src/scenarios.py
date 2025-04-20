import random


def generate_common_metrics():
    return {
        "cpu_usage": round(random.uniform(0, 100), 2),
        "memory_usage": round(random.uniform(0, 100), 2),
        "response_time": round(random.uniform(0.05, 5.0), 3),
        "availability": round(random.uniform(0.9, 1.0), 3),
        "cost": round(random.uniform(0.01, 1.0), 4),
        "rtt": round(random.uniform(1, 100), 2),
        "throughput": round(random.uniform(10, 1000), 2),
        "latency": round(random.uniform(1, 100), 2),
    }


def scenario_normal():
    metrics = generate_common_metrics()
    metrics["service_type"] = "web"
    return metrics


def scenario_high_load():
    metrics = generate_common_metrics()
    metrics["cpu_usage"] = round(random.uniform(90, 100), 2)
    metrics["memory_usage"] = round(random.uniform(85, 100), 2)
    metrics["response_time"] = round(random.uniform(3.0, 10.0), 3)
    metrics["latency"] = round(random.uniform(80, 200), 2)
    metrics["service_type"] = "database"
    return metrics


def scenario_low_availability():
    metrics = generate_common_metrics()
    metrics["availability"] = round(random.uniform(0.5, 0.8), 3)
    metrics["response_time"] = round(random.uniform(4.0, 12.0), 3)
    metrics["service_type"] = "storage"
    return metrics


def scenario_failure():
    metrics = generate_common_metrics()
    metrics["availability"] = 0.0
    metrics["response_time"] = None
    metrics["cpu_usage"] = 0.0
    metrics["memory_usage"] = 0.0
    metrics["throughput"] = 0.0
    metrics["latency"] = None
    metrics["rtt"] = None
    metrics["service_type"] = "unknown"
    return metrics
