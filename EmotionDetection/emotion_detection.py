import requests
import json

def get_dominant_emotion(emotion_dict):
    dominant_emotion_tuple = max(emotion_dict.items(), key=lambda x: x[1])
    return dominant_emotion_tuple[0]

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    result = requests.post(url, headers=headers, json=input_json)

    formatted_response = json.loads(result.text)

    emotions_dict = formatted_response['emotionPredictions'][0]['emotion']
    emotions_dict['dominant_emotion'] = get_dominant_emotion(emotions_dict)

    return emotions_dict


