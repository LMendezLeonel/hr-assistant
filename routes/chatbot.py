from flask import Blueprint, render_template, request, jsonify
from database.connection import get_connection
from config.settings import ANTHROPIC_API_KEY
import anthropic

chatbot_bp = Blueprint('chatbot', __name__)

def get_hr_context():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT e.name, e.position, e.salary, e.hire_date, d.name as department
        FROM employees e
        LEFT JOIN departments d ON e.department_id = d.id
        WHERE e.active = 1
    ''')
    employees = cursor.fetchall()

    cursor.execute('''
        SELECT e.name, v.start_date, v.end_date, v.days, v.status
        FROM vacations v
        JOIN employees e ON v.employee_id = e.id
    ''')
    vacations = cursor.fetchall()

    conn.close()

    context = "=== EMPLEADOS ACTIVOS ===\n"
    for emp in employees:
        context += f"- {emp['name']} | {emp['position']} | Depto: {emp['department']} | Salario: ${emp['salary']:,.0f} | Ingreso: {emp['hire_date']}\n"

    context += "\n=== VACACIONES ===\n"
    for vac in vacations:
        context += f"- {vac['name']} | Del {vac['start_date']} al {vac['end_date']} | {vac['days']} días | Estado: {vac['status']}\n"

    return context

@chatbot_bp.route('/chat')
def chat():
    return render_template('chatbot/chat.html')

@chatbot_bp.route('/chat/message', methods=['POST'])
def message():
    data = request.get_json()
    user_message = data.get('message', '')

    hr_context = get_hr_context()

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=f"""Sos un asistente de Recursos Humanos inteligente y amigable. 
Respondés preguntas sobre los empleados, departamentos y vacaciones de la empresa.
Usás los datos reales de la base de datos que se te proporcionan.
Respondés siempre en español, de forma clara y concisa.

Datos actuales de la empresa:
{hr_context}""",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"response": response.content[0].text})