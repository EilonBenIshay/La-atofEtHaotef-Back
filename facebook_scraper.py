import requests

def getPosts():
    posts = []
    facebook_request = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAGjIfPPdYsBO4rAvZA0ZCyrMrEwUV9Hf59Cb8ZCsSwHc2wv2xSIxuYQpzq6Bu81YSB7FmGXGeMM5KuY4tqeqFj0ntPTJh35RrrUPpaVqavEoIRgZCsEdnGpX6XZBV03tYJWqokvzWdMELZB1uvqRpRfnQe4CwzcX6thL0oZAaEMzpOQrWZCNrlTI5C74DTQtzy7WuxlMnLfmjbcXxJI8ZCYInDJUZCoYZD"
)
    
    name = facebook_request.json()['name']
    fbposts = facebook_request.json()['posts']['data']
    
    for data in fbposts[:-1]:
        picture = ""
        message = ""
        if 'full_picture' in data.keys():
            picture = data['full_picture']
        if 'message' in data.keys():
            message = data['message']
        
        posts.append({"userName" : name,
                      "imageURL" : picture,
                      "description" : message})
        
    return posts
