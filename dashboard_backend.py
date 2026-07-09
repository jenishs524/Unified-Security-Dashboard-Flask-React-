#!/usr/bin/env python3
"""
Unified Security Dashboard – Backend
Serves frontend and provides real‑time alerts via SocketIO.
"""

import time
import threading
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from data_generator import generate_alerts, generate_stats

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# In‑memory storage
alerts = generate_alerts(20)
stats = generate_stats()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/alerts')
def get_alerts():
    return jsonify(alerts)

@app.route('/api/stats')
def get_stats():
    return jsonify(stats)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('alerts', alerts)
    emit('stats', stats)

def background_alert_generator():
    """Generate a new random alert every 10 seconds and broadcast."""
    while True:
        time.sleep(10)
        new_alert = generate_alerts(1)[0]
        alerts.append(new_alert)
        if len(alerts) > 100:
            alerts.pop(0)
        # Update stats (simplified)
        stats['total_alerts'] += 1
        if new_alert['severity'] == 'Critical':
            stats['critical'] += 1
        elif new_alert['severity'] == 'High':
            stats['high'] += 1
        elif new_alert['severity'] == 'Medium':
            stats['medium'] += 1
        else:
            stats['low'] += 1
        socketio.emit('new_alert', new_alert)
        socketio.emit('stats', stats)

if __name__ == '__main__':
    # Start background thread for live alerts
    thread = threading.Thread(target=background_alert_generator, daemon=True)
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5001, debug=True, use_reloader=False)