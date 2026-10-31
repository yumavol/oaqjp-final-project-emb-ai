"""Flask server for the emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def get_emotion_detector():
    """Analyze the given text and return its emotion scores."""
    result = emotion_detector(request.args.get("textToAnalyze"))

    if result["dominant_emotion"] is None:
        return (" Invalid text! Please try again!", 200)

    report = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return (report, 200)

@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    