from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

#App metadata
APP_NAME = "devops-cicd-project"
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
APP_ENV = os.environ.get("APP_ENV", "development")

@app.route('/')
def home():
    return jsonify({
        "service": APP_NAME,
        "version": APP_VERSION,
        "env": APP_ENV,
        "status": "running",
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "healthy": True,
        "service": APP_NAME,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }), 200

@app.route('/metrics')
def metrics():
    return jsonify({
        "service": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
        "uptime": "running"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
