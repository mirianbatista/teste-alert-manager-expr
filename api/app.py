from flask import Flask, Response
from prometheus_client import Gauge, Counter, generate_latest

app = Flask(__name__)
# gauge = Gauge('teste_argos_gauge', 'Teste gauge')
counter = Counter('teste_argos_counter', 'Teste counter')

@app.route('/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

@app.route('/increase', methods=['GET'])
def increase():
    # gauge.inc()
    counter.inc()
    return "Increased gauge and counter value"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
