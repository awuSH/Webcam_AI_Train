# main.py

from routers.tell_skicounter import make_guess

image_path = "assets/test_other_skiareas/Bildschirmfoto 2024-05-02 um 11.34.23.png"
class_name, confidence_score = make_guess(image_path)
print("Class:", class_name)
print("Confidence Score:", confidence_score)
