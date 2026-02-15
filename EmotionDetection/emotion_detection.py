import requests
import json

def emotion_detector(text_to_analyze):
    """
    Using Watson NLP embedded library to perform emotion prediction on text
    """
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Seting the header with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    # Getting all emotions
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    anger = emotion['anger']
    disgust = emotion['disgust']
    fear = emotion['fear']
    joy = emotion['joy']
    sadness = emotion['sadness']
    # Find the highest score
    dominant_emotion = max(emotion, key=emotion.get)
    # Return the required output as dictionary
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}