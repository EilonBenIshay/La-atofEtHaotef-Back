import requests
from post import Post

def getPosts():
    posts = []
    facebook_request = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAWrjJSlXycBO6RtMPxQmvt3fhDuwYMPc8RF5Uee6ekD6csLhZCVRIFD4WTwxUxbUzybU6418sN16La6FzzmTgSI60VlyP5iwZBLPWnkMK9hcrXbdAUA0tPyJwrREMYTyGQ7wUIPwx7eLxmvT4ZBzeyrt5kQo82eGPuIAZAL4Q0mwL3DXgS595cw"
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
