import json
from flask import Flask, jsonify, render_template
import pyautogui
import qrcode_terminal
import socket

app = Flask(__name__)

def create_endpoint(route, method, keys):
    def func():
        try:
            pyautogui.hotkey(*keys)
            return jsonify({'message': f'{"+".join(keys).upper()} keys pressed successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    func.__name__ = '_'.join(keys)
    app.route(route, methods=[method])(func)

with open('static/endpoints.json') as f:
    endpoints = json.load(f)

for endp in endpoints:
    create_endpoint(endp['route'], endp['method'], endp['keys'])

@app.route('/endpoints.json')
def endpoints():
    return app.send_static_file('endpoints.json')
    
@app.route('/deck', methods=['GET'])
def buttons():
    return render_template('geek-deck.html')

if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    qr_code_data = f"http://{ip_address}:4999/deck"
    qrcode_terminal.draw(qr_code_data)
    app.run(host='0.0.0.0', port=4999)
