import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'change_this_secret_key')
csrf = CSRFProtect(app)

@app.route('/')
def home():
    return "¡Hola desde DevSecOps con Flask!"

if __name__ == '__main__':
    # Evitar debug=True en código productivo
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
