# CRUD pour les utilisateurs (réservé aux admins)
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.models.user import User
from app.forms.user_form import UserForm
from app import db
from app.utils.decorators import admin_required

user_bp = Blueprint("user", __name__, url_prefix="/users")

@user_bp.route("/")
@login_required
@admin_required
def index():
    users = User.query.all()
    return render_template("admin/users.html", users=users)

@user_bp.route("/create", methods=["GET", "POST"])
@login_required
@admin_required
def create():
    form = UserForm()
    if form.validate_on_submit():
        u = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            role=form.role.data
        )
        if form.password.data:
            u.set_password(form.password.data)
        else:
            # Default password if not provided, but in practice, generate or require
            u.set_password("default_password")  # Change in prod
        db.session.add(u)
        db.session.commit()
        flash("Utilisateur créé", "success")
        return redirect(url_for("user.index"))
    return render_template("admin/user_form.html", form=form)

@user_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(user_id):
    u = User.query.get_or_404(user_id)
    form = UserForm(obj=u)
    if form.validate_on_submit():
        u.username = form.username.data
        u.first_name = form.first_name.data
        u.last_name = form.last_name.data
        u.email = form.email.data
        u.role = form.role.data
        if form.password.data:
            u.set_password(form.password.data)
        db.session.commit()
        flash("Utilisateur mis à jour", "success")
        return redirect(url_for("user.index"))
    return render_template("admin/user_form.html", form=form, user=u)

@user_bp.route("/delete/<int:user_id>", methods=["POST"])
@login_required
@admin_required
def delete(user_id):
    u = User.query.get_or_404(user_id)
    db.session.delete(u)
    db.session.commit()
    flash("Utilisateur supprimé", "info")
    return redirect(url_for("user.index"))

# API minimal pour lister les utilisateurs (JSON)
@user_bp.route("/api", methods=["GET"])
@login_required
@admin_required
def api_list():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "first_name": u.first_name, "last_name": u.last_name, "email": u.email, "role": u.role} for u in users])