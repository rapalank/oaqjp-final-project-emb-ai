from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
server = Flask(__name__)

@server.route("/")
def render_index_page():
    return render_template('index.html')

@server.route('/emotionDetector')
def return_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_scores = emotion_detector(text_to_analyze)
    display_text = 'For the given statement, the system response is '
    display_text += f"'anger': {emotion_scores['anger']}, "
    display_text += f"'disgust': {emotion_scores['disgust']}, "
    display_text += f"'fear': {emotion_scores['fear']}, "
    display_text += f"'joy': {emotion_scores['joy']} and "
    display_text += f"'sadness': {emotion_scores['sadness']}. "
    display_text += f"The dominant emotion is <b>{emotion_scores['dominant_emotion']}</b>."
    return display_text

#    return("The dominant emotion is <b>joy</b>")

if __name__ == "__main__":
    server.run()