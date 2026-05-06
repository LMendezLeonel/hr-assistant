# HR Assistant 🏢🤖

A Human Resources management system with an integrated AI chatbot, built with Python Flask and Claude AI.

## 🚀 Live Demo
👉 [https://hr-assistant-a912.onrender.com](https://hr-assistant-a912.onrender.com)

## ✨ Features

- **Employee Management** — Create, update, and deactivate employees
- **Department Organization** — Organize staff across departments
- **Vacation Tracking** — Register and monitor vacation requests
- **AI Chatbot** — Ask questions about your workforce in natural language
  - *"How many employees are in the Technology department?"*
  - *"Who has the highest salary?"*
  - *"What vacation requests are pending?"*

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **AI:** Claude API (Anthropic)
- **Frontend:** HTML, CSS, JavaScript

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/LMendezLeonel/hr-assistant.git
cd hr-assistant
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Add your Anthropic API key to .env
```

5. Run the app
```bash
python app.py
```

6. Open your browser at `http://127.0.0.1:5000`

## 📁 Project Structure
hr-assistant/
├── app.py              # Main Flask application
├── config/             # Configuration and settings
├── database/           # DB connection and seed data
├── models/             # Data models
├── routes/             # Application routes
├── templates/          # HTML templates
└── static/             # CSS, JS, images

## 🤖 AI Chatbot

The chatbot uses Claude AI to answer questions about your employees in natural language. It automatically pulls real-time data from the database to provide accurate answers.

## 👨‍💻 Author

**Leonel Mendez**  
[LinkedIn](www.linkedin.com/in/leonel-mendez-3a6977210) · [GitHub](https://github.com/LMendezLeonel)