from flask import Flask, request
from instagram_scraper import get_all_posts
from facebook_scraper import getPosts
from flask_cors import CORS, cross_origin
import psycopg2 

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/')
@cross_origin()
def hello():
    return 'Hello, World!'

@app.route('/add_post', methods=['POST']) 
def addPost(): 
    conn = psycopg2.connect(database="sampledb", 
                            user="userW2X", 
                            password="3wDARjwQDHFToSw5", 
                            host="10.130.2.60", port="5432") 
  
    cur = conn.cursor() 
  
    # Get the data from the form 
    image = request.form['imageURL'] 
    description = request.form['description'] 
    userName = request.form['userName']
    mode = request.form['mode'] 
  
    # Insert the data into the table 
    cur.execute( 
        '''INSERT INTO items \ 
        (imageurl, username, description, mode) VALUES (%s, %s, %s, %s)''', 
        (image, userName, description, mode)) 
  
    # commit the changes 
    conn.commit() 

@app.route('/Instagram')
@cross_origin()
def getInstagramPage():
    USERNAMES = [ "otef.gaza", "logistic_center_", "ironswords_volunteers",
                  "aguda.sherut", "hashomer_hachadash", "ironswords_volunteers",
                  "onedaysv", "ivolunteer.il", "hitnadvout.ramat.hasharon",
                  "volunteer_jlm"]

    return get_all_posts(USERNAMES)

@app.route('/Facebook', methods=['GET'])
@cross_origin()
def getFacebookPage():
    mode = int(request.args.get('mode', 0))
    posts = getPosts()
    return [p.to_json() for p in posts if p.mode == mode]
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
