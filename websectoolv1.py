import requests

# This is an example of a simple security tool in Python that can be used to check for common vulnerabilities in websites:
# Please do change the url at the bottom of the script to scan whichever website you want!

def check_vulnerabilities(url):
    # Check for HTTP security headers
    response = requests.head(url)
    headers = response.headers

    security_headers = {
        "Strict-Transport-Security": False,
        "X-Content-Type-Options": False,
        "X-Frame-Options": False,
        "Content-Security-Policy": False,
        "X-XSS-Protection": False,
    }

    for header, required in security_headers.items():
        if header in headers:
            security_headers[header] = True

    print("Security Headers:")
    for header, status in security_headers.items():
        if status:
            print(f"✅ {header} is set")
        else:
            print(f"❌ {header} is NOT set")

    # Check for open ports
    common_ports = [80, 443, 8080, 8443]  # Add more ports if needed

    print("\nOpen Ports:")
    for port in common_ports:
        try:
            response = requests.get(f"{url}:{port}", timeout=2)
            print(f"✅ Port {port} is open")
        except requests.exceptions.RequestException:
            print(f"❌ Port {port} is closed")

    # Add more vulnerability checks as needed...

# Example usage
check_vulnerabilities("https://google.com")
