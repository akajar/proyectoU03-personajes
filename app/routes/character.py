from flask import Blueprint, render_template
from app.models.character import Character
from app.database import collection

character_route = Blueprint('character_route',__name__)

