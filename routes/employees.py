from flask import Blueprint, render_template, request, redirect, url_for
from database.connection import get_connection

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/employees')
def lista():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT e.id, e.name, e.email, e.phone, e.position, 
               e.salary, e.hire_date, d.name as department
        FROM employees e
        LEFT JOIN departments d ON e.department_id = d.id
        WHERE e.active = 1
        ORDER BY e.name
    ''')
    employees = cursor.fetchall()
    conn.close()

    return render_template('employees/lista.html', employees=employees)

@employees_bp.route('/employees/alta', methods=['GET', 'POST'])
def alta():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM departments")
    departments = cursor.fetchall()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        position = request.form['position']
        salary = request.form['salary']
        hire_date = request.form['hire_date']
        department_id = request.form['department_id']

        cursor.execute('''
            INSERT INTO employees (name, email, phone, position, salary, hire_date, department_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, position, salary, hire_date, department_id))
        conn.commit()
        conn.close()
        return redirect(url_for('employees.lista'))

    conn.close()
    return render_template('employees/alta/form.html', departments=departments)

@employees_bp.route('/employees/modificacion/<int:id>', methods=['GET', 'POST'])
def modificacion(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM departments")
    departments = cursor.fetchall()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        position = request.form['position']
        salary = request.form['salary']
        hire_date = request.form['hire_date']
        department_id = request.form['department_id']

        cursor.execute('''
            UPDATE employees 
            SET name=?, email=?, phone=?, position=?, salary=?, hire_date=?, department_id=?
            WHERE id=?
        ''', (name, email, phone, position, salary, hire_date, department_id, id))
        conn.commit()
        conn.close()
        return redirect(url_for('employees.lista'))

    cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
    employee = cursor.fetchone()
    conn.close()
    return render_template('employees/modificacion/form.html', employee=employee, departments=departments)

@employees_bp.route('/employees/baja/<int:id>', methods=['GET', 'POST'])
def baja(id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        cursor.execute("UPDATE employees SET active=0 WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('employees.lista'))

    cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
    employee = cursor.fetchone()
    conn.close()
    return render_template('employees/baja/confirm.html', employee=employee)