# CRUD pour les produits (admin)

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.models.product import Product
from app.forms.product_form import ProductForm
from app import db
from app.utils.decorators import admin_required
from datetime import datetime

product_bp = Blueprint("product", __name__, url_prefix="/products")

@product_bp.route("/")
def index():
    # liste publique des produits (template)
    products = Product.query.order_by(Product.timeS_in.desc()).all()
    return render_template("products/index.html", products=products)

@product_bp.route("/create", methods=["GET", "POST"])
@login_required
@admin_required
def create():
    form = ProductForm()
    if form.validate_on_submit():
        p = Product(
            type_p = form.type_p.data,
            designation_p = form.designation_p.data,
            prix_ht = form.prix_ht.data,
            date_in = form.date_in.data,
            stock_p = form.stock_p.data or 0
        )
        db.session.add(p)
        db.session.commit()
        flash("Produit ajouté", "success")
        return redirect(url_for("product.index"))
    return render_template("products/product_form.html", form=form)

@product_bp.route("/edit/<int:id_p>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(id_p):
    p = Product.query.get_or_404(id_p)
    form = ProductForm(obj=p)
    if form.validate_on_submit():
        p.type_p = form.type_p.data
        p.designation_p = form.designation_p.data
        p.prix_ht = form.prix_ht.data
        p.date_in = form.date_in.data
        p.stock_p = form.stock_p.data
        db.session.commit()
        flash("Produit mis à jour", "success")
        return redirect(url_for("product.index"))
    return render_template("products/product_form.html", form=form, product=p)

@product_bp.route("/delete/<int:id_p>", methods=["POST"])
@login_required
@admin_required
def delete(id_p):
    p = Product.query.get_or_404(id_p)
    db.session.delete(p)
    db.session.commit()
    flash("Produit supprimé", "info")
    return redirect(url_for("product.index"))

# API endpoints JSON (exemples)
@product_bp.route("/api", methods=["GET"])
def api_list():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@product_bp.route("/api/<int:id_p>", methods=["GET"])
def api_get(id_p):
    p = Product.query.get_or_404(id_p)
    return jsonify(p.to_dict())