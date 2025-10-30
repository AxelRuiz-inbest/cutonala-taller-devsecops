from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Lab 3 - Dependencias vulnerables"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'DevSecOps')
    return f"Hola, {name}!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
