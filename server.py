""" This is the server module of the Emotion Detector app. """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """ This function gets the text to be analyzed.
    Then calls the appropriate function to analyze.
    Then based on results returns output. """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and get the response
    response = emotion_detector(text_to_analyze)
    # Error handling
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    # Return a formatted string
    return f"""For the given statement, the system response is
    'anger': {response['anger']}, 
    'disgust': {response['disgust']}, 
    'fear': {response['fear']}, 
    'joy': {response['joy']} and 
    'sadness': {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    """ This function just shows the interface. """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
