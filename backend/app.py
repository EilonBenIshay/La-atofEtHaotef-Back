from flask import Flask
from controllers.posts_controller import posts_bp 

app = Flask(__name__)
app.register_blueprint(posts_bp)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
