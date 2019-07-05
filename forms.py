from flask import Flask, request
from flask_wtf import Form
from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Lengt

class PeopleForm(Form):
    """ Formulario de registro para personas  nuevas a la """
    nombre = 
    