import requests

def getPosts():
    posts = []
    facebook_request = requests.get(
 "https://graph.facebook.com/v20.0/me?fields=id%2Cname%2Cposts%7Bmessage%2Cfull_picture%7D&origin_graph_explorer=1&transport=cors&access_token=EAAGjIfPPdYsBO7hUSJqZAvefwIcBFejAIs59cYaRak7ENyPSbuDPlR09H0XmCfhYJM8VJwhfoKhgahWxJYefVsA6blBq12hop1LGEoSUFhcxe6ZAMSihdUlQ5aOPFDuckwPIdY0vXtqPHI0xhaPnZCRCFH5LUehikANyBg2GE6KX5mjl6x5EFLyg4qxOTZCVbcmSuwUm6ISiJTLxJMpu4CPj9oOz8nqJFH3TZAxZBXIoUvt6AydYKocU8BTM8P5AZDZD"
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
