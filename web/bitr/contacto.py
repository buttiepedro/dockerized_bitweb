from flask import Blueprint, Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

from bitr import mail

bp = Blueprint('contacto', __name__, url_prefix='/contacto')

@bp.route('/', methods=["GET", "POST"])
def contacto():

    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]

        msg = Message("Nuevo mensaje de contacto", sender=email, recipients=["buttiepedro.bit@gmail.com"])
        msg.body = f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}"
        mail.send(msg)

        flash("Mensaje enviado correctamente", "success")
        return redirect("/")

    return render_template('contacto.html')