from knowledge.rules import RULES


def calculate_risk(evidence_package):

    score = 100

    for observation in evidence_package["observations"]:

        rule = RULES.get(observation["title"])

        if not rule:
            continue

        weight = rule["weight"]

        if observation["status"] in ("Not Observed", "Expired"):

            if weight < 0:
                score += weight

        elif observation["status"] in ("Observed", "Valid"):

            if weight > 0:
                score += weight

    score = max(0, min(score, 100))

    if score >= 90:
        level = "Excellent"

    elif score >= 75:
        level = "Good"

    elif score >= 50:
        level = "Moderate"

    else:
        level = "Needs Review"

    return {
        "score": score,
        "level": level
    }