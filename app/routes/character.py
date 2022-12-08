from flask import Blueprint, render_template,flash, request
from app.models.character import Character
from app.database import collection

from requests import get

character_route = Blueprint('character_route',__name__)

@character_route.route('/')
def index():
    if collection.count_documents({}) == 0:
        flash("¡Falta cargar los datos! \U0001F62C","error")
        return render_template('index.html')
    
    page = request.args.get('page',1,type=int)
    characters,last_page = get_page(page)
    return render_template('index2.html', characters = characters, page = page, last_page = last_page)

def get_page(page, items_per_page = 20):
    last_page = get_last_page(items_per_page)
    if page == 1:
        cursor = collection.find().limit(items_per_page)
        return list(cursor),last_page
    
    last_id = (page-1)*items_per_page
    cursor = collection.find({'id':{'$gt': last_id}}).limit(items_per_page)
    return list(cursor), last_page

def get_last_page(page_size):
    documents = collection.count_documents({})
    if documents % page_size != 0:
        return documents//page_size + 1
    return documents // page_size

@character_route.route('/success')
def load_data():
    if collection.count_documents({}) != 0:
        return index()
    get_character_from_api()
    flash('DATOS CARGADOS CON EXITO :D','success')
    return index()

def get_character_from_api():
    API_URL = 'https://rickandmortyapi.com/api/character'
    data = get_json_api(API_URL)
    insert_to_database(data)
    
def get_json_api(url):
    try:
        data = get(url).json()
    except:
        data = None
    return data

def insert_to_database(data):
    for result in data['results']:
        insert_character(result)
    
    if data['info']['next'] is None:
        return
    
    next_data = get_json_api(data['info']['next'])
    insert_to_database(next_data)

def insert_character(data):
    character = Character(
        id = data['id'],
        name = data['name'],
        status = data['status'],
        species = data['species'],
        type = data['type'],
        gender = data['gender'],
        origin = data['origin']['name'],
        location = data['location']['name'],
        image = data['image'],
        first_episode = get_json_api(data['episode'][0])['name']
    )
    
    collection.insert_one(character.to_json())

@character_route.route('/profile/<int:id>')
def view_character_profile(id):
    return f"Profile #{id}"