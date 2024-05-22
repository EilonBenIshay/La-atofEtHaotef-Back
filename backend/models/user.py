class user:
    def __init__(self, userName, password, catagories,  desription, likedByList, LikedUsersList, activeChatList, image):
        self.userName = userName
        self.password = password
        self.catagories = catagories
        self.desription = desription
        self.likedByList = likedByList
        self.LikedUsersList= LikedUsersList
        self.activeChatList = activeChatList
        self.image = image
    
    def __init__(self, userName, password, catagories,  desription):
        self.userName = userName
        self.password = password
        self.catagories = catagories
        self.desription = desription
        self.likedByList = []
        self.LikedUsersList= []
        self.activeChatList = []
        self.image = None
