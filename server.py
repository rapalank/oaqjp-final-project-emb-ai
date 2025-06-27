""" 
Flask Server for NLP Emotion Detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
server = Flask(__name__)

@server.route("/")
def render_index_page():
    """
    Displays the main page for emotion detection.
    """

    return render_template('index.html')

@server.route('/emotionDetector')
def return_emotion():
    """
    Displays the emotion of the input text, and an error message for empty text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_scores = emotion_detector(text_to_analyze)
    print(emotion_scores)
    if emotion_scores['dominant_emotion'] is None:
        return "<b> Invalid text! Please try again! </b>"

    display_text = 'For the given statement, the system response is '
    display_text += f"'anger': {emotion_scores['anger']}, "
    display_text += f"'disgust': {emotion_scores['disgust']}, "
    display_text += f"'fear': {emotion_scores['fear']}, "
    display_text += f"'joy': {emotion_scores['joy']} and "
    display_text += f"'sadness': {emotion_scores['sadness']}. "
    display_text += f"The dominant emotion is <b>{emotion_scores['dominant_emotion']}</b>."
    return display_text

if __name__ == "__main__":
    server.run()
