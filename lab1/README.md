Lab 1 - API vulnerable a SQL Injection (Flask + SQLite)

Estructura:
- vulnerable/: código con vulnerabilidad
- fixed/: código corregido que vamo

Instrucciones:
1. Entrar en vulnerable/
2. python -m venv .venv && source .venv/bin/activate
3. pip install -r requirements.txt
4. python setup_db.py
5. python app.py
6. curl "http://127.0.0.1:5000/user?name=Alice"
7. haremos un curl "http://127.0.0.1:5000/user?name=' OR '1'='1" 
    curl --get --data-urlencode "name=' OR '1'='1" "http://127.0.0.1:5000/user"
8. Revisar bandit: bandit -r .

Correción:
1. Entrar en fixed/
2. pip install -r requirements.txt
3. python app.py
4. Repetir pruebas; la inyección ya no debe funcionar.

Notas:
- Este laboratorio es exclusivamente educativo.
- Ejecutarlo solo en entornos controlados.
