from database.connection import get_connection

def seed_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Verificar si ya hay datos
    cursor.execute("SELECT COUNT(*) FROM departments")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return  # Ya tiene datos, no volver a insertar

    # Departamentos
    departments = [
        ("Tecnología", "Desarrollo y sistemas"),
        ("Recursos Humanos", "Gestión de personal"),
        ("Ventas", "Comercial y clientes"),
        ("Finanzas", "Contabilidad y finanzas"),
    ]
    cursor.executemany(
        "INSERT INTO departments (name, description) VALUES (?, ?)",
        departments
    )

    # Empleados
    employees = [
        ("Carlos García",    "carlos@empresa.com",  "1134567890", "Desarrollador Backend",  85000, "2022-03-15", 1),
        ("María López",      "maria@empresa.com",   "1145678901", "Diseñadora UX",           75000, "2021-07-01", 1),
        ("Juan Pérez",       "juan@empresa.com",    "1156789012", "Analista de RRHH",         65000, "2023-01-10", 2),
        ("Ana Martínez",     "ana@empresa.com",     "1167890123", "Vendedora Senior",         70000, "2020-11-20", 3),
        ("Luis Rodríguez",   "luis@empresa.com",    "1178901234", "Contador",                 72000, "2022-08-05", 4),
        ("Sofia Fernández",  "sofia@empresa.com",   "1189012345", "Desarrolladora Frontend",  80000, "2023-04-18", 1),
    ]
    cursor.executemany(
        '''INSERT INTO employees 
           (name, email, phone, position, salary, hire_date, department_id) 
           VALUES (?, ?, ?, ?, ?, ?, ?)''',
        employees
    )

    # Vacaciones
    vacations = [
        (1, "2024-02-01", "2024-02-15", 14, "aprobada"),
        (2, "2024-03-10", "2024-03-20", 10, "aprobada"),
        (3, "2024-04-05", "2024-04-10",  5, "pendiente"),
        (4, "2024-05-01", "2024-05-07",  6, "aprobada"),
    ]
    cursor.executemany(
        '''INSERT INTO vacations 
           (employee_id, start_date, end_date, days, status) 
           VALUES (?, ?, ?, ?, ?)''',
        vacations
    )

    conn.commit()
    conn.close()
    print("✅ Base de datos poblada con datos de prueba")