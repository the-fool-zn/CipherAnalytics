import pickle
import json
import tensorflow as tf

# Load your existing trained model
model = tf.keras.models.load_model("backend/ai/cnn_model.keras")

# Convert to TFLite (much smaller, much lighter to run)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("backend/ai/cnn_model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Saved cnn_model.tflite")

# Extract tokenizer word index (so we don't need TF just to unpickle it)
with open("backend/ai/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("backend/ai/tokenizer_word_index.json", "w") as f:
    json.dump(tokenizer.word_index, f)

print("✅ Saved tokenizer_word_index.json")

# Extract label encoder classes (so we don't need scikit-learn at runtime)
with open("backend/ai/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

with open("backend/ai/label_classes.json", "w") as f:
    json.dump(label_encoder.classes_.tolist(), f)

print("✅ Saved label_classes.json")