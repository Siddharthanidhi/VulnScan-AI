def detect_technologies(headers):

    technologies = []

    headers = {k.lower(): v for k, v in headers.items()}

    server = headers.get("server", "")

    if "cloudfront" in server.lower():
        technologies.append("Amazon CloudFront")

    if "cloudflare" in server.lower():
        technologies.append("Cloudflare")

    if "nginx" in server.lower():
        technologies.append("Nginx")

    if "apache" in server.lower():
        technologies.append("Apache")

    if "iis" in server.lower():
        technologies.append("Microsoft IIS")

    if headers.get("x-amzn-waf-action"):
        technologies.append("AWS WAF")

    return technologies