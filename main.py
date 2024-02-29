from flask import Flask, render_template, request, flash, g
from forms import EmployForm
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db   
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
        

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route("/index", methods=["GET", "POST"])
def index():
    empleados = EmployForm(request.form)

    if request.method == "POST":
        employObj = Alumnos(
            id=empleados.id.data,
            nombre=empleados.nombre.data,
            direccion=empleados.direccion.data,
            telefono=empleados.telefono.data,
            email=empleados.email.data,
            sueldo=empleados.sueldo.data
        )
        db.session.add(employObj)
        db.session.commit()

    return render_template("index.html", form=empleados)


@app.route("/ABC_Completo", methods=["GET","POST"])
def ABC_Completo():
    employ_form= EmployForm(request.form)
    employObj = Alumnos.query.all()
    return render_template("ABC_Completo.html", empleado=employ_form, empleados=employObj)

@app.route("/eliminar.html", methods=["GET","POST"])
def eliminar():
    return render_template("eliminar.html")

@app.route("/editar.html", methods=["GET","POST"])
def editar():
    return render_template("editar.html")

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()    
    app.run()