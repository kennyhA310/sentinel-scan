# Sentinel Scan

## Overview
Sentinel Scan is a modular Python-based cybersecurity scanner designed to perform basic network reconnaissance and vulnerability identification against a target host.

The project combines:
- Port scanning
- Banner grabbing
- CVE detection
- JSON-based reporting

This repository demonstrates a simple security workflow for identifying exposed services, collecting service metadata, and mapping findings to known vulnerabilities.

## Features
- Scans a target host for open ports
- Performs banner grabbing on discovered services
- Analyzes service information for potential CVE matches
- Generates structured output for reporting
- Uses a modular project layout for easier extension and maintenance

## Project Structure
```text
sentinel-scan/
├── core/
│   └── engine.py
├── detection/
│   ├── analyzer.py
│   └── cve_db.py
├── modules/
│   ├── banner_grab.py
│   └── port_scan.py
├── reports/
├── utils/
│   ├── logger.py
│   └── report.py
└── main.py
