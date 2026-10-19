
from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
import base64
from src.cnnClassifier.utils.common import decodeimage
from src.cnnClassifier.pipelines.predict import PredictionPipeline

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    exit_code = os.system("python main.py")

    if exit_code == 0:
        return "Training done successfully!"

    return "Training failed!", 500


@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    data = request.get_json()

    if not data or "image" not in data:
        return jsonify({"error": "Image is required"}), 400

    decodeimage(data["image"], clApp.filename)
    result = clApp.classifier.predict()

    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080)
