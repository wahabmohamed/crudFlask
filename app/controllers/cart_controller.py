# Gestion du panier (réservé aux utilisateurs normaux)
from flask import Blueprint, session, jsonify, request, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from app.models.product import Product

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

def _get_cart():
    # stocker le panier dans la session (simplifié)
    return session.setdefault("cart", {})

@cart_bp.route("/")
@login_required
def index():
    # afficher panier de l'utilisateur connecté
    cart = _get_cart()
    items = []
    total = 0
    for pid, qty in cart.items():
        p = Product.query.get(pid)
        if p:
            subtotal = p.prix_ht * qty
            items.append({"product": p, "quantity": qty, "subtotal": subtotal})
            total += subtotal
    return render_template("user/cart.html", items=items, total=total)

@cart_bp.route("/add/<int:product_id>", methods=["POST"])
@login_required
def add(product_id):
    p = Product.query.get_or_404(product_id)
    if p.stock_p <= 0:
        flash("Produit en rupture de stock", "danger")
        return redirect(url_for("product.index"))
    cart = _get_cart()
    qty = int(request.form.get("quantity", 1))
    if qty > p.stock_p:
        qty = p.stock_p
    cart[str(product_id)] = cart.get(str(product_id), 0) + qty
    session["cart"] = cart
    flash("Produit ajouté au panier", "success")
    return redirect(url_for("product.index"))

@cart_bp.route("/update/<int:product_id>", methods=["POST"])  # Nouveau: update quantity
@login_required
def update(product_id):
    cart = _get_cart()
    qty = int(request.form.get("quantity", 1))
    if qty <= 0:
        cart.pop(str(product_id), None)
    else:
        cart[str(product_id)] = qty
    session["cart"] = cart
    flash("Quantité mise à jour", "info")
    return redirect(url_for("cart.index"))

@cart_bp.route("/remove/<int:product_id>", methods=["POST"])
@login_required
def remove(product_id):
    cart = _get_cart()
    cart.pop(str(product_id), None)
    session["cart"] = cart
    flash("Produit retiré du panier", "info")
    return redirect(url_for("cart.index"))