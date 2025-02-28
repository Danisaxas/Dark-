from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from config import MONGO_URI

auth = Blueprint("auth", __name__)
client = MongoClient(MONGO_URI)
db = client["chatbot_db"]
users = db["users"]

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = users.find_one({"email": email})

        if user and check_password_hash(user["password"], password):
            session["user_id"] = str(user["_id"])
            return redirect(url_for("chat"))
        else:
            flash("Correo o contraseña incorrectos", "danger")

    return render_template("login.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        
        if users.find_one({"email": email}):
            flash("El correo ya está registrado", "danger")
        else:
            users.insert_one({"email": email, "password": password})
            flash("Registro exitoso, ahora puedes iniciar sesión", "success")
            return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("auth.login"))
