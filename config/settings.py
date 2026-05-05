import os
from dotenv import load_dotenv

load_dotenv()

# Anthropic
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Flask
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "clave-por-defecto")
DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"

# Base de datos
DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'hr.db')