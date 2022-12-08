class Character:
    def __init__(
            self,
            id,
            name,
            status,
            species,
            type,
            gender,
            origin,
            location,
            image,
            episodes):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episodes = episodes
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'type': self.type,
            'gender': self.gender,
            'origin': self.origin,
            'location': self.location,
            'image': self.image,
            'episodes': self.episodes
        }