from flask import Flask, jsonify, render_template
import pyautogui
import qrcode_terminal
import socket

app = Flask(__name__)
    
@app.route('/stage', methods=['POST'])
def stage():
    try:
        pyautogui.hotkey('command', 'ctrl', 't')
        return jsonify({'message': 'COMMAND+CONTROL+T keys pressed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/microphone', methods=['POST'])
def camera():
    try:
        pyautogui.hotkey('command', 'd')
        return jsonify({'message': 'COMMAND+D keys pressed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/camera', methods=['POST'])
def microphone():
    try:
        pyautogui.hotkey('command', 'e')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/start_stop_slides', methods=['POST'])
def start_stop_slides():
    try:
        pyautogui.hotkey('command', 'p')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/left_arrow', methods=['POST'])
def left_arrow():
    try:
        pyautogui.hotkey('left')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/right_arrow', methods=['POST'])
def right_arrow():
    try:
        pyautogui.hotkey('right')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/grid', methods=['POST'])
def grid():
    try:
        pyautogui.hotkey('command', 'ctrl', 'j')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/floating_tile', methods=['POST'])
def floating_tile():
    try:
        pyautogui.hotkey('command', 'ctrl', 'k')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/active_speaker', methods=['POST'])
def active_speaker():
    try:
        pyautogui.hotkey('command', 'ctrl', 'l')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/scene', methods=['POST'])
def scene():
    try:
        pyautogui.hotkey('command', 'v')
        return jsonify({'message': 'Yes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/deck', methods=['GET'])
def buttons():
    return render_template('geek-deck.html')

if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    qr_code_data = f"http://{ip_address}:4999/deck"
    qrcode_terminal.draw(qr_code_data)
    app.run(host='0.0.0.0', port=4999)
