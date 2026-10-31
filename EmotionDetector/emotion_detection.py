import requests
import json

def emotion_detector(text_to_analyze):
    response = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', 
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}, 
        json={ "raw_document": { "text": text_to_analyze } }
    )
    data_json = json.loads(response.text)
    emotion = data_json['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion, key=emotion.get)

    formatted_response = {
        'anger': emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return formatted_response 


# result = emotion_detector(text_to_analyze="I am so sad")

# print(result)

 