import requests
from post import Post

def getPosts():
    posts = []
    facebook_request = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAGjIfPPdYsBO4ycAvAA1GCa9jYoSFrw5DOlufmZBRHpWZA5C2KGhTu96kWfXkkTAk5gvZAZCR445JWLpbnLZBFOAEYTNJ9ZAzvoTj7ZA8uTYHTwSj1BWYhaq2AFLVNqvaY3kJA1E9j2F5HYEtjA4diBw6reXYzx5vRQ6XsSPUATwL467rL97bDhZAz3"
)
    
    name = facebook_request.json()['name']
    fbposts = facebook_request.json()['posts']['data']
    
    for data in fbposts[:-1]:
        picture = ""
        message = ""
        createdDate = ""
        if 'full_picture' in data.keys():
            picture = data['full_picture']
        if 'message' in data.keys():
            message = data['message']
        if 'created_date' in data.keys():
            createdDate = data['created_date']
        
        if "מחפש " in message:
            mode = 1
        elif "למסירה " in message:
            mode = 0
        else:
            mode = 2
        
        posts.append(Post(name, createdDate, picture, message, mode, "Facebook"))
    return posts
