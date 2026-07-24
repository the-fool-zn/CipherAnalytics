import os
import time
import pickle
import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AI_DIR = os.path.join(BASE_DIR, "ai")

MODEL_PATH = os.path.join(AI_DIR, "cnn_model.keras")
TOKENIZER_PATH = os.path.join(AI_DIR, "tokenizer.pkl")
LABEL_PATH = os.path.join(AI_DIR, "label_encoder.pkl")

# --------------------------------------------------
# Load model once
# --------------------------------------------------

print("Loading CipherAnalytics AI Model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model Loaded Successfully.")

with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

with open(LABEL_PATH, "rb") as f:
    label_encoder = pickle.load(f)

MAX_LEN = 512

# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict(ciphertext: str):

    start = time.time()

    # Remove spaces and convert to lowercase
    ciphertext = ciphertext.strip().replace(" ", "").lower()

    # Convert ciphertext to sequence
    sequence = tokenizer.texts_to_sequences([ciphertext])

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LEN,
        padding="post",
        truncating="post"
    )

    # -----------------------------------------------
    # Numerical features (same format as training)
    # -----------------------------------------------

    cipher_bytes = len(ciphertext) // 2

    key_length = cipher_bytes * 8      # bits
    cipher_length = cipher_bytes       # bytes

    extra = np.array(
        [[key_length, cipher_length]],
        dtype=np.float32
    )

    extra = np.repeat(
        extra[:, np.newaxis, :],
        MAX_LEN,
        axis=1
    )

    cnn_input = np.concatenate(
        [
            padded[..., np.newaxis],
            extra
        ],
        axis=2
    )

    # -----------------------------------------------
    # Prediction
    # -----------------------------------------------

    probabilities = model.predict(
        cnn_input,
        verbose=0
    )[0]

    best_index = np.argmax(probabilities)

    algorithm = label_encoder.inverse_transform(
        [best_index]
    )[0]

    confidence = float(
        probabilities[best_index] * 100
    )

    top_indices = np.argsort(probabilities)[::-1][:3]

    top_predictions = []

    for idx in top_indices:

        top_predictions.append(
            {
                "name": label_encoder.inverse_transform([idx])[0],
                "score": round(
                    float(probabilities[idx] * 100),
                    2
                )
            }
        )

    inference_time = round(
        time.time() - start,
        4
    )

    return {
        "algorithm": algorithm,
        "confidence": round(confidence, 2),
        "top_predictions": top_predictions,
        "inference_time": inference_time
    }