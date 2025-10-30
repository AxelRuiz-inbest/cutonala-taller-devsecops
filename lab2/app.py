from flask import Flask
import config 

app = Flask(__name__)

@app.route('/')
def home():
    return "Lab2: revisa la variable API_KEY"

@app.route('/show-key')
def show_key():
    return {
        "api_key": config.API_KEY,
        "note": "Este endpoint no debería exponer secretos"
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
