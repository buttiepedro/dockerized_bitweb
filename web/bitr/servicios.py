from flask import Blueprint, render_template, request, redirect, url_for, g, jsonify


bp = Blueprint('servicios', __name__, url_prefix='/servicios')

@bp.route('/')
def servicios():
    return render_template('servicios.html')