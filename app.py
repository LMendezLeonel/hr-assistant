from flask import Flask, render_template
from config.settings import SECRET_KEY, DEBUG
from database.connection import init_db, get_connection
from database.seed import seed_db

app = Flask(__name__)
app.secret_key = SECRET_KEY

with app.app_context():
    init_db()
    seed_db()

from routes.employees import employees_bp
from routes.chatbot import chatbot_bp

app.register_blueprint(employees_bp)
app.register_blueprint(chatbot_bp)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees WHERE active = 1")
    total_employees = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM departments")
    total_departments = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM vacations WHERE status = 'pendiente'")
    total_vacations = cursor.fetchone()[0]

    conn.close()

    return render_template('index.html',
        total_employees=total_employees,
        total_departments=total_departments,
        total_vacations=total_vacations
    )

if __name__ == '__main__':
    app.run(debug=DEBUG)