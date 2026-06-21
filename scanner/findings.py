HEADER_FINDINGS = {
    "Content-Security-Policy": {
        "severity": "Medium",
        "owasp": "A05: Security Misconfiguration",
        "description": "Missing CSP may increase risk of Cross-Site Scripting attacks.",
        "recommendation": "Implement Content-Security-Policy header."
    },
    "Strict-Transport-Security": {
        "severity": "High",
        "owasp": "A05: Security Misconfiguration",
        "description": "Missing HSTS allows downgrade attacks.",
        "recommendation": "Enable Strict-Transport-Security."
    },
    "X-Frame-Options": {
        "severity": "Medium",
        "owasp": "A05: Security Misconfiguration",
        "description": "Missing protection against clickjacking attacks.",
        "recommendation": "Enable X-Frame-Options."
    },
    "X-Content-Type-Options": {
        "severity": "Low",
        "owasp": "A05: Security Misconfiguration",
        "description": "Browser may incorrectly interpret content types.",
        "recommendation": "Enable X-Content-Type-Options."
    },
    "Referrer-Policy": {
        "severity": "Low",
        "owasp": "A01: Broken Access Control",
        "description": "Sensitive URLs may leak via referrer headers.",
        "recommendation": "Configure Referrer-Policy."
    }
}