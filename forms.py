from wtforms import Form
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, FloatField, TelField
from wtforms import EmailField
# Aqui agregaremos los campos que sean obligatorios y el email
from wtforms.validators import DataRequired, Email, Length

class EmployForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre=StringField("Nombre", [validators.DataRequired(message="El nombre es requerido"), validators.length(min=4,max=20, message="Ingresa un nombre de entre 4 a 20 letras")])
    direccion=StringField("Dirección", [validators.DataRequired(message="La dirección es requerida")])
    telefono=StringField("Telefono", [validators.DataRequired(message="El campo es requerido"), validators.length(min=10,max=10, message="El telefono debe tener 10 digitos")])
    email=EmailField("Email", [validators.DataRequired(message=("El campo es requerido")), validators.Email('Ingrese un correo valido') ])
    sueldo=FloatField("Sueldo", [validators.DataRequired(message="El campo es requerido")])