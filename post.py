import json

class Post:
    def __init__(self, userName, dateTime, imageURL, description, mode, source):
        self.userName = userName
        self.datetime = dateTime
        self.imageURL = imageURL
        self.description = description
        self.mode = mode
        self.source = source
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        json_data = json.loads(json_str)
        return cls(**json_data)
