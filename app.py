#!/usr/bin/env python3
"""
Simple Python Hello World application for Docker containerization
"""
from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Hello World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            text-align: center;
            padding: 40px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Hello from Docker!</h1>
        <p>This is a Python Flask application running in a Docker container.</p>
        <p>Container ID: {{ container_id }}</p>
        <p>Python Version: {{ python_version }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    import platform
    container_id = os.environ.get('HOSTNAME', 'Unknown')
    python_version = platform.python_version()
    return render_template_string(HTML_TEMPLATE, 
                                 container_id=container_id,
                                 python_version=python_version)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

