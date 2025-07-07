# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Frontend'den gelen istekler için CORS'u etkinleştir
CORS(app)

@app.route('/api')
def get_message():
    return jsonify(message="Merhaba Kubernetes! Sample Projem nasıl", version="1.3")

if __name__ == '__main__':
    # Konteyner içinde 0.0.0.0 üzerinden erişilebilir olmalı
    app.run(host='0.0.0.0', port=5000)