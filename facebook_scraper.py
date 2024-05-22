import requests

def getPosts():
    posts = []
    facebook_request = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAGjIfPPdYsBOzrWAi4JX74kd801Gh2ZBnYOpRMautU7WfMQuyG0N6hLvSkB70lAAmpnQFTuGBkTvjSOviTmrddJw4fPDsBCyZBBtNTcGx7BpsDJdhz8BPsOF3t7cn2ZCE8cUWHbeuvFFv2488GOojujHq3QQZBiKmHbh6APpVxlucclneNCrcHPdZAsZB5QAC7v5Pc644ZC9ve8vUpBejR3fdiI0WjhcL1DKahPako4UEBZCZBNrZBDYsRNypZBJ1vGwZDZD"
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
