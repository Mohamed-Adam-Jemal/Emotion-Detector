import requests
import json

def dominant_emotion(emotions):
    max_value = 0
    dominant_emotion = None
    
    for emotion, score in emotions.items():
        if score > max_value:
            max_value = score
            dominant_emotion = emotion
    
    return dominant_emotion

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominent_emotion = dominant_emotion(formatted_response['emotionPredictions'][0]['emotion'])
        return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy':joy_score, 'sadness':sadness_score, 'dominent_emotion': dominent_emotion}
    
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy':None, 'sadness':None, 'dominent_emotion': None}