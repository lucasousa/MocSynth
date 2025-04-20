import random
from datetime import datetime, timedelta

import src.scenarios as base

SCENARIO_FUNCS = [
    base.scenario_normal,
    base.scenario_high_load,
    base.scenario_low_availability,
    base.scenario_failure,
]


def generate_synthetic_data(
    days: int, interval_minutes: int, proportions: list, providers: list
):
    assert sum(proportions) == 100, "A soma das proporções deve ser 100%"

    start_time = datetime.now()
    total_points = int((days * 24 * 60) / interval_minutes)

    scenario_distribution = []
    for i, percent in enumerate(proportions):
        scenario_distribution.extend([i] * int(percent * total_points / 100))
    random.shuffle(scenario_distribution)

    data = []
    current_time = start_time

    for idx in range(total_points):
        if idx < len(scenario_distribution):
            scenario_idx = scenario_distribution[idx]
        else:
            scenario_idx = random.choice(range(len(SCENARIO_FUNCS)))

        provider = random.choice(providers)
        service = random.choice(provider["services"])

        entry = SCENARIO_FUNCS[scenario_idx]()
        entry.update(
            {
                "timestamp": current_time.isoformat(),
                "provider": provider["name"],
                "service": service,
            }
        )
        data.append(entry)

        current_time += timedelta(minutes=interval_minutes)

    return data
