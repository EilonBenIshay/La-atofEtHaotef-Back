import requests

def getPosts():
    posts = []
    facebook_request = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAGjIfPPdYsBO6YqZBMUGWz7QZBKH98VplDedASodeQ32IOnmaHh2ivOAsOZAZClZC75eNNfe4JTTfmevjZBoiIJ7eP12baY48TZBmAF5rV6W2XrBP97dZBCapJ5iUveznD50rqzomzMIpHX7Tn2HYr7ekR8IbmveoTE30ZBeIy9s4bBC2EZCSZBZCZCLoWZCfBA6Ih8baBnLH7ZCjgL6ZBFqO9xFXsQ9B6kiZAl9nPWHtdZAIq2ADJHMgZBrDkxZCdB"
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
