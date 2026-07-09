📁 Unified Security Dashboard (Flask + React)

Description
A full‑stack web dashboard that aggregates alerts and statistics from all other projects. Uses Flask for the backend and a modern frontend with Chart.js. Real‑time updates via SocketIO (or polling).

Key Features

    Live alerts with timestamps, severity, and project origin.

    Statistics cards (total, critical, high, medium, low).

    Severity pie chart and project bar chart.

    Real‑time updates every 10 seconds (mock data generator).

    REST API endpoints: /api/alerts, /api/stats.

Technologies

    Flask, Flask‑SocketIO, eventlet (or gevent), Jinja2, Chart.js.

Prerequisites

    Python 3, Flask, SocketIO, etc.

    Modern browser.

Installation
bash

sudo apt install python3-flask python3-flask-socketio python3-jinja2
# or pip install flask flask-socketio eventlet jinja2

Usage

    Run the backend:
    bash

python dashboard_backend.py

    Open http://127.0.0.1:5001 (or the port set in the script).

    Watch live alerts and charts update automatically.

Sample Output
Terminal shows client connections and alert generation.
Browser displays the dashboard with live data.

Notes

    The background thread generates a new alert every 10 seconds.

    You can replace mock data with real integrations to your security tools.

    If SocketIO fails, use the polling version (dashboard_backend_simple.py).
