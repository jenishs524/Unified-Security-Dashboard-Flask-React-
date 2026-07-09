#!/usr/bin/env python3
"""
Mock data generator for the Unified Security Dashboard.
Generates random alerts and scan results.
"""

import random
import datetime

project_names = [
    "Network Mapper", "NIDS", "Honeypot", "CIS Auditor", "OSINT Recon",
    "Cloud Scanner", "SIEM", "Email Validator", "Password Vault",
    "Bug Bounty Recon", "Malware Traffic", "WAF", "JWT Auth",
    "Android Frida", "AD Mapper", "SOAR", "Ransomware Sim",
    "Wireless Audit", "Forensics Imager", "Network Fuzzer",
    "Container Scanner", "Password Cracker", "DNS Tunnel Detector",
    "OSINT Scraper", "SSL Tester", "Phishing Cloner", "CVSS Prioritizer",
    "EDR Simulator", "Threat Intel Aggregator"
]

severities = ["Critical", "High", "Medium", "Low"]

def generate_alerts(count=10):
    alerts = []
    for i in range(count):
        alerts.append({
            "id": i,
            "project": random.choice(project_names),
            "severity": random.choice(severities),
            "message": f"Alert from {random.choice(project_names)}",
            "timestamp": datetime.datetime.now().isoformat()
        })
    return alerts

def generate_stats():
    return {
        "total_alerts": random.randint(50, 200),
        "critical": random.randint(5, 20),
        "high": random.randint(10, 30),
        "medium": random.randint(20, 50),
        "low": random.randint(20, 40),
        "projects": len(project_names)
    }