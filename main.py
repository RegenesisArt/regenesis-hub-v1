from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sovereign Hub Online'

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/log', methods=['POST'])
def log_session():
    log_data = request.get_json()
    if not log_data:
        return jsonify({'error': 'No data provided'}), 400
    print(f"[CMHP LOG] {log_data}")
    with open('session_log.txt', 'a') as f:
        f.write(json.dumps(log_data) + '\n')
    return jsonify({'status': 'success', 'message': 'Session logged'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
