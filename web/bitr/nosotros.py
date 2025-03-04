from flask import Blueprint, render_template, request, redirect, url_for, g, jsonify


bp = Blueprint('nosotros', __name__, url_prefix='/nosotros')

@bp.route('/')
def nosotros():
    return render_template('nosotros.html')