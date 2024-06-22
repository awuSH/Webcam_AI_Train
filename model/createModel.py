#createModelSkiing.py
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

# Setze die Lernrate auf 0.0001
learning_rate = 0.001
train_data = "../assets/testdata"
test_data = "../assets/traindata"
model_name = "model_skicount"
# Erstelle den Adam-Optimierer mit der festgelegten Lernrate
optimizer = Adam(learning_rate=learning_rate)

# Create ImageDataGenerator object for data augmentation and normalization
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=5, #small range because webcam an static picture
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.05,
    zoom_range=0.05,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(
    rescale=1./255
)
# Generators for training and test data
train_generator = train_datagen.flow_from_directory(
    train_data,  # Path to your training data
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_data,  # Path to your test data folder
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)

# Model architecture setup
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(3, activation='softmax')  # Adjusted to the number of classes detected
])

# Compile the model
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Define early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train model with early stopping callback
history = model.fit(
    train_generator,
    epochs=50,
    validation_data=test_generator,
    callbacks=[early_stopping]  # Pass the early stopping callback to the fit method
)

# Save the trained model
model.save('model/{model_name}.h5')

# Optionally, print out the history to see how the model performed during training
print(history.history)
