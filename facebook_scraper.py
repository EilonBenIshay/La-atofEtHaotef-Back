import requests
from post import Post

def getPosts():
    posts = []
    facebook_request = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAGjIfPPdYsBO5ZBoFEh8Y9OBK8EM17zlGj84WMiHpJlZBGFmscGLUSad85GofjMH0HyAsJBSNBPiI8OR5DNmdAE6vQeubL9AZAFWPitThMHqBUUEY7daMH0uxvZCyID6jpvb3RENXFwky4OJmTU1hQedq0ZBujy98bc5Q6uHyrE0vmpMceqLJ1eS"
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
