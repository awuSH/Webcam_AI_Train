from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import numpy as np
import os
from sklearn.metrics import confusion_matrix, classification_report
network_path = '/Volumes/netzlaufwerk/88_Coding/00_Datasets/dataset_skipiste_crowded/testdata_brightness/'

def load_image(img_path, target_size=(150, 150)):
    """
    Lädt ein Bild von einem Dateipfad und skaliert es auf die angegebene Größe.
    
    Args:
        img_path (str): Der Dateipfad des Bildes.
        target_size (tuple): Die Zielgröße des Bildes. Standardmäßig (150, 150).
        
    Returns:
        numpy.ndarray: Das geladene und skalierte Bild als Numpy-Array.
    """
    img = load_img(img_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = img_array / 255.0  # Normalisierung der Pixelwerte auf den Bereich [0, 1]
    return img_array

# Modell laden
model = load_model('model/trained_model_skicount.h5')
test_data = network_path

# Testdaten vorbereiten
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    test_data,
    target_size=(150, 150),
    batch_size=20,
    class_mode='categorical',  # Korrekte Schreibweise
    shuffle=False)  # Wichtig: nicht mischen, um Labels und Vorhersagen zu vergleichen

# Vorhersagen machen
predictions = model.predict(test_generator)
predicted_classes = np.argmax(predictions, axis=1)  # Umwandlung in Klassenindizes
true_classes = test_generator.classes

# Verwirrungsmatrix und Klassifizierungsbericht ausgeben
cm = confusion_matrix(true_classes, predicted_classes)
cr = classification_report(true_classes, predicted_classes, target_names=test_generator.class_indices.keys())

# Vorhersagen für jedes Testbild machen
for i in range(len(test_generator.filenames)):
    img_path = test_generator.filepaths[i]
    img_label = test_generator.labels[i]
    img = load_image(img_path)  # Lade das Testbild
    
    # Vorhersage für das Bild machen
    prediction = model.predict(np.expand_dims(img, axis=0))
    predicted_class = np.argmax(prediction)
    
# Öffne eine Textdatei zum Schreiben
with open('predictions.txt', 'w') as file:
    # Schreibe die Überschrift
    file.write("Pfad, pred_Klasse, ist_Klasse, Vorhersage (wahr/falsch)\n")
    
    # Schreibe die Vorhersagen für jedes Testbild
    for i in range(len(test_generator.filenames)):
        img_path = test_generator.filepaths[i]
        img_label = test_generator.labels[i]
        img = load_image(img_path)  # Lade das Testbild

        # Vorhersage für das Bild machen
        prediction = model.predict(np.expand_dims(img, axis=0))
        predicted_class = np.argmax(prediction)

        # Überprüfe, ob die Vorhersage korrekt ist
        is_correct = "wahr" if predicted_class == img_label else "falsch"
        
        # Schreibe die Informationen in die Datei
        file.write(f"{img_path}, {predicted_class}, {img_label}, {is_correct}\n")

print("Vorhersagen wurden in 'predictions.txt' gespeichert.")
with open('test_report.txt','w') as file:
    file.write("Klassifizierungsbericht:\n" + cr)
    file.write("\nVerwirrungsmatrix:\n" + str(cm))
# Ausgabe der Metriken
print("Verwirrungsmatrix:\n", cm)
print("Klassifizierungsbericht:\n", cr)
