#!/usr/bin/env python3
from flask import Flask, render_template_string, jsonify
import random
import time
from datetime import datetime

app = Flask(__name__)

# Mock data
alerts = []
severities = ["Critical", "High", "Medium", "Low"]
projects = ["NIDS", "Honeypot", "SIEM", "EDR", "WAF", "Scanner", "Vault"]

# Generate some initial alerts
for i in range(10):
    alerts.append({
        "id": i,
        "project": random.choice(projects),
        "severity": random.choice(severities),
        "message": f"Alert from {random.choice(projects)}",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/')
def dashboard():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head><title>Security Dashboard</title>
<style>
body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #0b0e14; color: #cdd6f4; padding:20px; }
h1 { color: #f9e2af; }
.alert { background: #1e2430; margin:6px 0; padding:10px; border-left:4px solid #f38ba8; border-radius:4px; }
.timestamp { color: #89b4fa; }
.severity-Critical { color:#dc3545; }
.severity-High { color:#fd7e14; }
.severity-Medium { color:#ffc107; }
.severity-Low { color:#28a745; }
</style>
<script>
function fetchAlerts() {
    fetch('/api/alerts')
        .then(r => r.json())
        .then(data => {
            const container = document.getElementById('alerts');
            container.innerHTML = '';
            data.slice().reverse().forEach(a => {
                const div = document.createElement('div');
                div.className = 'alert';
                div.innerHTML = `
                    <div>
                        <span class="timestamp">${a.timestamp}</span>
                        <span class="severity-${a.severity}">${a.severity}</span>
                        <strong>${a.project}</strong> – ${a.message}
                    </div>
                `;
                container.appendChild(div);
            });
        });
}
setInterval(fetchAlerts, 3000);
window.onload = fetchAlerts;
</script>
</head>
<body>
    <h1>🔐 Unified Security Dashboard</h1>
    <div id="alerts"></div>
</body>
</html>
    ''')

@app.route('/api/alerts')
def get_alerts():
    return jsonify(alerts)

@app.route('/api/new_alert', methods=['POST'])
def add_alert():
    new_alert = {
        "id": len(alerts),
        "project": random.choice(projects),
        "severity": random.choice(severities),
        "message": f"Alert from {random.choice(projects)}",
        "timestamp": datetime.now().isoformat()
    }
    alerts.append(new_alert)
    if len(alerts) > 100:
        alerts.pop(0)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)