import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    
    def predict(self):
        model = load_model(
            os.path.join("artifacts", "training", "model.h5")
        )

        test_image = image.load_img(
            self.filename,
            target_size=(224, 224)
        )

        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        probabilities = model.predict(test_image, verbose=0)
        class_index = int(np.argmax(probabilities, axis=1)[0])

        print("Probabilities:", probabilities)
        print("Predicted class index:", class_index)

        if class_index == 1:
            prediction = "Healthy"
        else:
            prediction = "Coccidiosis"

        return [{
            "image": prediction,
            "probabilities": probabilities[0].tolist(),
            "class_index": class_index
        }]

