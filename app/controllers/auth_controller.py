from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app.forms.profile_form import ProfileForm
from app.models.user import User
from app import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u and u.check_password(form.password.data):
            login_user(u)
            flash("Connexion réussie", "success")
            return redirect(url_for("product.index"))
        flash("Identifiants invalides", "danger")
    return render_template("login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_user or existing_email:
            flash("Nom d'utilisateur ou email déjà utilisé", "danger")
            return render_template("register.html", form=form)
        u = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            role="user"
        )
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash("Inscription réussie. Vous pouvez vous connecter.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Déconnecté", "info")
    return redirect(url_for("auth.login"))

@auth_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        if form.password.data:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash("Profil mis à jour", "success")
        return redirect(url_for("auth.profile"))
    return render_template("user/profile.html", form=form, user=current_user)