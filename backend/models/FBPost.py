import json

class FBPost:
    def __init__(self, userName, imageURL, description):
        self.userName = userName
        self.imageURL = imageURL
        self.description = description
        
    def to_json(self):
        return json.dumps({"userName": self.userName, "imageURL": self.imageURL, "description":self.description})

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data['userName'], data['imageURL'], data['description'])

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"Post(userName={self.userName}, imageURL={self.imageURL}, description={self.description})"