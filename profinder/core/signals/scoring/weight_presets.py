from typing import Dict


def get_weights(objective: str) -> Dict[str, float]:
    objective = objective.lower()
    presets = {
        "awareness": {
            "engagement": 0.25,
            "story": 0.25,
            "reach": 0.40,
            "reliability": 0.10,
        },
        "engagement": {
            "engagement": 0.60,
            "story": 0.20,
            "reach": 0.10,
            "reliability": 0.10,
        },
        "storytelling": {
            "engagement": 0.30,
            "story": 0.60,
            "reach": 0.10,
            "reliability": 0.10,
        },
    }
    return presets.get(objective, presets["awareness"])

