from flask import Blueprint, render_template,flash
from app.models.character import Character
from app.database import collection

character_route = Blueprint('character_route',__name__)

@character_route.route('/')
def index():
    if collection.count_documents({}) == 0:
        flash("¡Falta cargar los datos! \U0001F62C","error")
        return render_template('index.html')
    
    characters = collection.find()
    return render_template('index2.html', characters = characters)

@character_route.route('/success')
def charge_data():
    
    
    flash("DATOS CARGADOS CON EXITO :D","success")
    return index()