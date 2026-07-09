#!/usr/bin/env python3
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head><title>Security Dashboard</title></head>
<body>
    <h1>🔐 Unified Security Dashboard</h1>
    <p>Dashboard is live!</p>
    <p>Current time: {{ time }}</p>
</body>
</html>
"""

@app.route('/')
def index():
    from datetime import datetime
    return render_template_string(html, time=datetime.now().isoformat())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)