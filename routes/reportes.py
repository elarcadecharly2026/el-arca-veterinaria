from flask import Blueprint, render_template, request
from sqlalchemy import func
from datetime import datetime
from models import Sale, Expense
from database import SessionLocal

reportes_bp = Blueprint("reportes", __name__)

@reportes_bp.route("/reportes", methods=["GET","POST"])
def reportes():
    db = SessionLocal()

    try:
        inicio = request.form.get("inicio")
        fin = request.form.get("fin")

        if inicio and fin:
            inicio = datetime.fromisoformat(inicio)
            fin = datetime.fromisoformat(fin)
        else:
            inicio = datetime(datetime.now().year, datetime.now().month, 1)
            fin = datetime.now()

        ventas = db.query(func.sum(Sale.total)).filter(
            Sale.created_at.between(inicio, fin)
        ).scalar() or 0

        utilidad = db.query(func.sum(Sale.utilidad)).filter(
            Sale.created_at.between(inicio, fin)
        ).scalar() or 0

        gastos = db.query(func.sum(Expense.amount)).filter(
            Expense.created_at.between(inicio, fin)
        ).scalar() or 0

        facturado = db.query(func.sum(Sale.total)).filter(
            Sale.cfdi_id != None
        ).scalar() or 0

        no_facturado = ventas - facturado
        utilidad_neta = utilidad - gastos

        return render_template("reportes.html",
            ventas=ventas,
            utilidad=utilidad,
            gastos=gastos,
            utilidad_neta=utilidad_neta,
            facturado=facturado,
            no_facturado=no_facturado,
            inicio=inicio,
            fin=fin
        )

    finally:
        db.close()