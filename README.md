# Global MUN 2025 Website

A **professional Model United Nations (MUN) website** built with **Flask and Jinja2**, featuring a modern UI, online registration, schedule, committees, and admin panel.

---

## 🏆 Project Overview

This website is designed for organizing a MUN conference and includes the following:

- **Home Page**: Hero section, event tagline, quick info, and call-to-action.
- **About Page**: Information about MUN and this year's theme.
- **Committees Page**: List of committees, topics, and chairs.
- **Registration Page**: Online form for delegates to register.
- **Schedule Page**: Event agenda with table of activities.
- **Contact Page**: Contact information and social media links.
- **Admin Panel**: View registrations (login-protected).
- **Login System**: Admin login for secure access.
- **Flash Messages**: Registration success popup on the same page.
- **Responsive Design**: Mobile-friendly layout with clean UI.

---

## 💻 Tech Stack

- **Backend**: Python 3, Flask, Flask-SQLAlchemy  
- **Frontend**: HTML, CSS, Jinja2 templates  
- **Database**: SQLite  
- **Extras**: Flash messages, session-based login

---

## 📁 Project Structure

mun_website/
│
├── app.py # Flask main application
├── requirements.txt # Python dependencies
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── about.html
│ ├── committees.html
│ ├── registration.html
│ ├── schedule.html
│ ├── contact.html
│ ├── admin.html
│ └── admin_login.html
└── static/
├── css/
│ └── style.css
└── images/
└── banner.jpg


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd mun_website

2. Create virtual environment
python -m venv venv

3. Activate virtual environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Run the Flask app
python app.py

6. Open in browser
http://127.0.0.1:5000/

🔐 Admin Panel

Login page: /admin/login

View registrations: /admin/registrations

Logout: /admin/logout

📝 Features

Fully responsive and professional design

Registration form with flash message popup

Database storage for registrations (SQLite)

Admin login and protected admin panel

Home, About, Committees, Schedule, Contact pages

Easy to customize colors, images, and themes
