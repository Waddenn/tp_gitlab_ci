from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Connexion PostgreSQL
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "flask_db")
DB_USER = os.getenv("DB_USER", "flask_user")
DB_PASS = os.getenv("DB_PASS", "flask_password")

@app.route("/")
def home():
    return "Bienvenue sur mon application Flask CI/CD !"

@app.route("/db")
def db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
        )
        return "Connexion à la base de données réussie !"
    except Exception as e:
        return f"Erreur de connexion : {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
