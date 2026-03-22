from detection.cve_db import CVE_DATABASE


def analyze_results(results):
    print("\n[!] Analyzing results...")

    ports = results.get('ports', [])
    banners = results.get('banners', {})

    for port in ports:
        if port in CVE_DATABASE:
            vuln = CVE_DATABASE[port]

            print(f"[{vuln['risk']}] Port {port} ({vuln['service']})")
            print(f"        CVE: {vuln['cve']}")
            print(f"        Issue: {vuln['description']}")

    for port, banner in banners.items():
        banner_lower = banner.lower()
        if "ftp" in banner_lower:
            print(f"[WARNING] FTP service detected on port {port}")

        if "ssh" in banner_lower:
            print(f"[INFO] SSH detected on port {port}")