SEVERITY_WEIGHTS = {
    "High": 20,
    "Medium": 10,
    "Low": 5
}


def calculate_score(findings):

    score = 100

    for finding in findings:

        severity = finding["severity"]

        score -= SEVERITY_WEIGHTS.get(
            severity,
            5
        )

    return max(score, 0)


def get_risk_level(score):

    if score >= 85:
        return "Low Risk"

    elif score >= 60:
        return "Medium Risk"

    return "High Risk"