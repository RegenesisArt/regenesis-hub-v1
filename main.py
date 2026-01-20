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

@app.route('/latest-session', methods=['GET'])
def get_latest_session():
    try:
        with open('session_log.txt', 'r') as f:
            lines = f.readlines()
            if not lines:
                return jsonify({'error': 'No sessions found'}), 404
            latest = json.loads(lines[-1].strip())
            return jsonify(latest), 200
    except FileNotFoundError:
        return jsonify({'error': 'No session log file'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Corrupted session data'}), 500
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
