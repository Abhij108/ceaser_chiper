from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app) 
 
 
def ceaser_chiperE(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char == char.upper():
                start = ord('A')
                result += chr((ord(char)-start+shift)%26+start)
            else:
                start = ord('a')
                result += chr((ord(char)-start+shift)%26+start)
 
            
        else:
            result+=char
           
 
    return(result)
 
 
def ceaser_chiperD(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char == char.upper():
                start = ord('A')
                result += chr((ord(char)-start-shift)%26+start)
            else:
                start = ord('a')
                result += chr((ord(char)-start-shift)%26+start)
 
            
        else:
            result+=char
           
 
    return(result)
 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 
@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        text = data.get('text', '')
        shift = int(data.get('shift', 0))
        
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        result = ceaser_chiperE(text, shift)
        return jsonify({'result': result, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
 
 
@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        text = data.get('text', '')
        shift = int(data.get('shift', 0))
        
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        result = ceaser_chiperD(text, shift)
        return jsonify({'result': result, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
 
 
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'Server is running'}), 200
 
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)