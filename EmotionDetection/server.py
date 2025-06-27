from flask import Flask

server = Flask(__name__)

@server.route("/")
def render_index_page():
    return render_template('index.html')

@server.route('/emotionDetector')
def return_emotion():
    return("The dominant emotion is <b>joy</b>")

