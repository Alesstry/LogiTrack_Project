from flask import Flask, request, jsonify

app = Flask(__name__)
telemetry_logs = []

@app.route('/api/telemetry/report', methods=['POST'])
def telemetry_report():
    raw_payload = request.get_json()
    if not raw_payload:
        return jsonify({"error": "Empty payload"}), 400

    # Vulnerabilidad: Sin validación de entrada (M-01)
    telemetry_logs.append(raw_payload)
    return jsonify({"status": "success", "message": "Data received"}), 200

if __name__ == '__main__':
    # Vulnerabilidad: debug=True (H-01)
    app.run(host='0.0.0.0', port=5000, debug=True)