from flask import Blueprint
from models.Post import *

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/GetPosts')
def getPosts():
    posts = []
    post1 = Post("omer", "url","omer is omer")
    post2 = Post("efrat", "url","efrat is lopez")
    post3 = Post("eilon", "url","eilon is bored")
    posts.append(str(post1))
    posts.append(str(post2))
    posts.append(str(post3))
    return posts

@posts_bp.route('/about')
def about():
    return 'About page'
