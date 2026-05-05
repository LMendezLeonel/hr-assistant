# Estructura del Proyecto - HR Assistant

```
hr-assistant/
│
├── app.py                        # Punto de entrada, inicializa Flask
│
├── config/
│   ├── __init__.py
│   └── settings.py               # Configuración general (DB, API keys)
│
├── database/
│   ├── __init__.py
│   ├── connection.py             # Conexión a SQLite
│   └── seed.py                   # Datos de prueba iniciales
│
├── models/
│   ├── __init__.py
│   ├── employee.py               # Modelo Empleado (CRUD)
│   ├── department.py             # Modelo Departamento
│   └── vacation.py               # Modelo Vacaciones/Ausencias
│
├── routes/
│   ├── __init__.py
│   ├── employees.py              # Rutas: alta / baja / modificación / lista
│   └── chatbot.py                # Ruta del chat con IA
│
├── templates/
│   ├── index.html                # Dashboard principal
│   ├── partials/
│   │   ├── navbar.html           # Barra de navegación (se reutiliza)
│   │   └── footer.html           # Pie de página (se reutiliza)
│   ├── employees/
│   │   ├── lista.html            # Tabla con todos los empleados
│   │   ├── alta/
│   │   │   └── form.html         # Formulario para agregar empleado
│   │   ├── baja/
│   │   │   └── confirm.html      # Confirmación antes de eliminar
│   │   └── modificacion/
│   │       └── form.html         # Formulario para editar empleado
│   └── chatbot/
│       └── chat.html             # Interfaz del chatbot
│
├── static/
│   ├── css/
│   │   └── style.css             # Estilos globales
│   ├── js/
│   │   ├── main.js               # JS general
│   │   └── chat.js               # Lógica del chat en tiempo real
│   └── img/                      # Imágenes e íconos
│
├── .env                          # Variables secretas (NO subir a GitHub)
├── .env.example                  # Ejemplo de variables (SÍ subir)
├── .gitignore                    # Archivos ignorados por Git
├── requirements.txt              # Dependencias Python
└── README.md                     # Documentación del proyecto
```

## Flujo de la app

1. Usuario entra al dashboard → ve lista de empleados
2. Puede dar de alta / modificar / dar de baja empleados
3. Desde cualquier pantalla puede abrir el chatbot
4. El chatbot consulta la DB y responde con IA (Claude API)
