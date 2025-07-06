# 🏥 Hospital Patient Records (Flask + SQL)

A simple and beginner-friendly CRUD web application built using **Flask**, **SQLite**, and **Bootstrap** to manage hospital patient records. This project was created as part of an internship task to demonstrate backend + frontend integration using databases.

---

## 🚀 Features

- View all patients
- Add a new patient
- Edit patient details
- Delete a patient record
- Clean UI using Bootstrap

---

## 📂 Folder Structure
```
Project 1/
│
├── app.py                 # Main Flask app
├── config.py              # Flask configuration (DB & secret key)
├── models.py              # SQLAlchemy database models
├── forms.py               # Flask-WTF form definitions
├── requirements.txt       # List of required Python libraries
├── hospital.db            # SQLite database (auto-created)
│
├── templates/             # HTML templates
│   ├── layout.html
│   ├── index.html
│   ├── add_patient.html
│   └── edit_patient.html
│
└── static/                # Custom CSS
    └── styles.css
```

---

## 🧰 Tech Stack

- Python 3
- Flask
- SQLite (can be switched to PostgreSQL)
- SQLAlchemy ORM
- Bootstrap 5 (via CDN)
- Flask-WTF for form handling

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <repo_url>
cd "Project 1"
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
```
#### Activate it:
#### Windows:
```bash
venv\Scripts\activate
```
#### macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```



