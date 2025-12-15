from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)

# 🔐 Secret key (required for sessions)
app.secret_key = "super-secret-admin-key"  # change later

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registrations.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -------------------------
# Database Model
# -------------------------
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    school = db.Column(db.String(100))
    committee = db.Column(db.String(50))
    notes = db.Column(db.Text)

# -------------------------
# Admin Credentials (change these)
# -------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "mun123"

# -------------------------
# Login Required Decorator
# -------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated_function

# -------------------------
# Public Routes
# -------------------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/committees")
def committees():
    return render_template("committees.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# -------------------------
# Registration
# -------------------------
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        entry = Registration(
            name=request.form["name"],
            email=request.form["email"],
            school=request.form["school"],
            committee=request.form["committee"],
            notes=request.form.get("notes")
        )
        db.session.add(entry)
        db.session.commit()

        flash("🎉 Registration Successful!", "success")
        return redirect(url_for("registration"))

    return render_template("registration.html")


# -------------------------
# Admin Login
# -------------------------
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        if (
            request.form["username"] == ADMIN_USERNAME
            and request.form["password"] == ADMIN_PASSWORD
        ):
            session["admin_logged_in"] = True
            return redirect(url_for("view_registrations"))
        else:
            error = "Invalid username or password"
    return render_template("admin_login.html", error=error)

# -------------------------
# Admin Logout
# -------------------------
@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))

# -------------------------
# Protected Admin Page
# -------------------------
@app.route("/admin/registrations")
@login_required
def view_registrations():
    data = Registration.query.all()
    return render_template("admin.html", data=data)

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
