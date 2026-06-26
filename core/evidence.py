from datetime import datetime

from analyzers.observations import build_observations

from engine.risk import calculate_risk
from engine.recommendations import generate_recommendations
from engine.limitations import generate_limitations


def build_evidence_package(context):

    evidence = {

        "scan": {

            "target": context.target,

            "timestamp": context.started_at.isoformat()

        },

        "collectors": context.collector_results,

        "observations": [],

        "risk": {},

        "recommendations": [],

        "limitations": []

    }

    evidence["observations"] = build_observations(
        evidence
    )

    evidence["risk"] = calculate_risk(
        evidence
    )

    evidence["recommendations"] = generate_recommendations(
        evidence
    )

    evidence["limitations"] = generate_limitations(
        evidence
    )

    return evidence