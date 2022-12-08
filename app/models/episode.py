from datetime import datetime

class Episode:
    def __init__(self, id, name, air_date, episode, characters):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'air_date': self.air_date,
            'episode': self.episode,
            'characters': self.characters
        }