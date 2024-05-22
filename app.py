from flask import Flask
from instagram_scraper import get_all_posts
from controllers.posts_controller import getPosts
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/Instagram')
@cross_origin()
def getInstagramPage():
    USERNAMES = [ "otef.gaza", "logistic_center_", "ironswords_volunteers",
                  "aguda.sherut", "hashomer_hachadash", "ironswords_volunteers",
                  "onedaysv", "ivolunteer.il", "hitnadvout.ramat.hasharon",
                  "volunteer_jlm"]

    return get_all_posts(USERNAMES)

@app.route('/Facebook')
@cross_origin()
def getFacebookStuff():
    return getPosts()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
