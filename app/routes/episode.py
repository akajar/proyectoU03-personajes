from flask import Blueprint, abort, render_template, request
from app.models.episode import Episode
from app.database import db

from requests import get

episode_route = Blueprint('episode_route',__name__)

@episode_route.route('/episode/<int:id>')
def episode_details(id, count = db['episodes'].count_documents({})):
    if count == 0:
        get_episodes()
        return ""
    
    if id <= count:
        data = db['episodes'].find_one({'id':id})
        return render_template('episode.html', episode = data, count=count)
    return abort(404)

def get_episodes():
    API_URL = 'https://rickandmortyapi.com/api/episode'
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
        insert_episode(result)
    
    if data['info']['next'] is None:
        return
    
    next_data = get_json_api(data['info']['next'])
    insert_to_database(next_data)

def insert_episode(data):
    episode = Episode(
        id = data['id'],
        name = data['name'],
        air_date = data['air_date'],
        episode = data['episode'],
        characters = [x[42:] for x in data['characters']]
    )
    print(episode.to_json())
    db['episodes'].insert_one(episode.to_json())
    
def import_characters(id_list):
    for id in id_list:
        character = db['characters'].find_one({'id':id})
        yield character