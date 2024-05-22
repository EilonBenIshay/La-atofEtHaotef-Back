from models.Post import Post
import requests

@staticmethod
def getPosts():
    print("here")
    posts = []
    idk = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAGjIfPPdYsBO6yls0BeZCdAp92Q232eKr1ZB06alk8ysO7f6KL51Vvpw6ePvATsNkSrLEB7Ca1ZAhrEq0DRYcazWD7L9hxsd1WVV3CBJqAyZCC5xsafaY4YlYAygOYFIIrNoUsHCgcsAZCQKhMeXqJwOeKt6mursjUdlIGbuWkXshVnkn0uAI1aPHulztIVDwmOZCl8M7YldsDssmcl8LuwxKvuarlqcHBpZAZBnCPWFrAZCxLHDPMkh"
)
    
    name = idk.json()['name']
    fbposts = idk.json()['posts']['data']
    
    for data in fbposts[:-1]:
        picture = ""
        message = ""
        if 'full_picture' in data.keys():
            picture = data['full_picture']
        if 'message' in data.keys():
            message = data['message']
        
        posts.append(str(Post(name, picture, message)))
        
    return posts
