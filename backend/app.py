from controllers.posts_controller import posts_bp 
from flask import Flask
from instagram_scraper import get_all_posts

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/Instagram')
def getInstagramPage():
    USERNAMES = [ "otef.gaza", "logistic_center_", "ironswords_volunteers",
                  "aguda.sherut", "hashomer_hachadash", "ironswords_volunteers",
                  "onedaysv", "ivolunteer.il", "hitnadvout.ramat.hasharon",
                  "volunteer_jlm"]

    return get_all_posts(USERNAMES)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)