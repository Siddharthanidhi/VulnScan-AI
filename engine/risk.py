def calculate_risk(evidence_package):

    score = 100

    observations = evidence_package["observations"]

    for observation in observations:

        title = observation["title"]
        status = observation["status"]

        if title == "Content-Security-Policy" and status == "Not Observed":
            score -= 10

        elif title == "Strict-Transport-Security" and status == "Observed":
            score += 5

        elif title == "X-Frame-Options" and status == "Not Observed":
            score -= 5

        elif title == "X-Content-Type-Options" and status == "Not Observed":
            score -= 5

        elif title == "Referrer-Policy" and status == "Not Observed":
            score -= 3

        elif title == "TLS Certificate" and status == "Valid":
            score += 5

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