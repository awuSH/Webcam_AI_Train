from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("model/trained_model_skicount.h5", compile=False)

# Extrahiere die Klassennamen aus dem Modell

class_names = ['much', 'none', 'some']  # Stelle sicher, dass die Reihenfolge korrekt ist

def make_guess(image_path):
    data = np.ndarray(shape=(1, 150, 150, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    size = (150, 150)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
   # image.save("temp_resized_image.jpg")  # Bild speichern
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)  # Der höchste Wert gibt die Klasse an
    class_name = class_names[index]  # Name der Klasse aus dem Array
    confidence_score = prediction[0][index]  # Vertrauenswert der Vorhersage
    return class_name, confidence_score

