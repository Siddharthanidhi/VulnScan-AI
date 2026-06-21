import streamlit as st

from scanner.headers import check_headers
from scanner.cookies import check_cookies
from scanner.admin import find_admin_pages
from scanner.analyzer import build_findings
from scanner.scoring import calculate_score, get_risk_level
from scanner.certificate import get_certificate_info

st.set_page_config(
    page_title="VulnScan AI",
    layout="wide"
)

st.title("🛡️ VulnScan AI")
st.caption("Website Security Assessment Platform")

st.write(
    """
    This tool performs passive security assessment by analyzing
    certificates, security headers, cookies, and exposed endpoints.

    Findings are observations and should be manually validated.
    """
)

url = st.text_input(
    "Target Website",
    placeholder="https://example.com"
)

if st.button("Start Assessment"):

    if not url:
        st.warning("Please enter a website URL.")
        st.stop()

    with st.spinner("Analyzing target..."):

        header_data = check_headers(url)

        if not header_data["success"]:
            st.error(header_data["error"])
            st.stop()

        certificate = get_certificate_info(url)

        cookies = check_cookies(url)

        admin_pages = find_admin_pages(url)

        findings = build_findings(
            header_data["headers"]
        )

        score = calculate_score(
            findings
        )

        risk = get_risk_level(
            score
        )

    # ==========================
    # DASHBOARD METRICS
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Security Score",
            score
        )

    with col2:
        st.metric(
            "Issues Found",
            len(findings)
        )

    with col3:
        st.metric(
            "Risk Level",
            risk
        )

    st.divider()

    # ==========================
    # CERTIFICATE SECTION
    # ==========================

    st.subheader("🔐 SSL/TLS Certificate")

    if certificate["success"]:

        cert_col1, cert_col2 = st.columns(2)

        with cert_col1:

            st.write(
                f"**Issued To:** {certificate['issued_to']}"
            )

            st.write(
                f"**Issuer:** {certificate['issuer']}"
            )

            st.write(
                f"**Valid From:** {certificate['valid_from']}"
            )

        with cert_col2:

            st.write(
                f"**Valid Until:** {certificate['valid_until']}"
            )

            st.write(
                f"**Days Remaining:** {certificate['days_remaining']}"
            )

            if certificate["expired"]:
                st.error(
                    "❌ Certificate Expired"
                )
            else:
                st.success(
                    "✅ Certificate Valid"
                )

    else:

        st.error(
            certificate["error"]
        )

    st.divider()

    # ==========================
    # SECURITY FINDINGS
    # ==========================

    st.subheader("🚨 Security Findings")

    if findings:

        for finding in findings:

            severity = finding["severity"]

            if severity == "High":

                st.error(
                    f"🔴 {finding['title']}"
                )

            elif severity == "Medium":

                st.warning(
                    f"🟡 {finding['title']}"
                )

            else:

                st.info(
                    f"🔵 {finding['title']}"
                )

            with st.expander("View Details"):

                st.write(
                    f"**OWASP:** {finding['owasp']}"
                )

                st.write(
                    f"**Description:** {finding['description']}"
                )

                st.write(
                    f"**Recommendation:** {finding['recommendation']}"
                )

    else:

        st.success(
            "No findings detected."
        )

    st.divider()

    # ==========================
    # SECURITY HEADERS
    # ==========================

    st.subheader("📋 Security Headers")

    for header, present in header_data["headers"].items():

        if present:

            st.success(
                f"✅ {header}"
            )

        else:

            st.error(
                f"❌ {header}"
            )

    st.divider()

    # ==========================
    # COOKIE ANALYSIS
    # ==========================

    st.subheader("🍪 Cookie Analysis")

    if cookies:

        for cookie in cookies:

            if cookie["secure"]:

                st.success(
                    f"{cookie['name']} - Secure"
                )

            else:

                st.warning(
                    f"{cookie['name']} - Not Secure"
                )

    else:

        st.info(
            "No cookies detected."
        )

    st.divider()

    # ==========================
    # ADMIN ENDPOINTS
    # ==========================

    st.subheader("🔍 Administrative Endpoints")

    if admin_pages:

        for page in admin_pages:

            st.warning(page)

    else:

        st.success(
            "No common admin endpoints detected."
        )

    st.divider()

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    st.subheader("💡 Recommendations")

    recommendations = []

    for header, present in header_data["headers"].items():

        if not present:

            recommendations.append(
                f"Enable {header}"
            )

    if admin_pages:

        recommendations.append(
            "Review administrative endpoint exposure."
        )

    if recommendations:

        for recommendation in recommendations:

            st.write(
                f"• {recommendation}"
            )

    else:

        st.success(
            "No recommendations at this time."
        )