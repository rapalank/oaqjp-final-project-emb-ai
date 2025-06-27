import requests
import sys

def emotion_detector(text_to_analyse : str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers = headers, json = payload)

    if response.status_code == 400:
        keys = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]
        return dict.fromkeys(keys, None)
    else: 
        emotion_scores = response.json()['emotionPredictions'][0]['emotion']
        highest_value_key = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = highest_value_key 
    return emotion_scores
