import os
import time
import json
import numpy as np
from ai_edge_litert.interpreter import Interpreter

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AI_DIR = os.path.join(BASE_DIR, "ai")

MODEL_PATH = os.path.join(AI_DIR, "cnn_model.tflite")
WORD_INDEX_PATH = os.path.join(AI_DIR, "tokenizer_word_index.json")
LABEL_CLASSES_PATH = os.path.join(AI_DIR, "label_classes.json")

# --------------------------------------------------
# Load model once
# --------------------------------------------------

print("Loading CipherAnalytics AI Model (TFLite)...")

interpreter = Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Model Loaded Successfully.")

with open(WORD_INDEX_PATH, "r") as f:
    word_index = json.load(f)

with open(LABEL_CLASSES_PATH, "r") as f:
    label_classes = json.load(f)

MAX_LEN = 512

# --------------------------------------------------
# Manual tokenizer (replicates Keras Tokenizer behavior)
# --------------------------------------------------

def texts_to_sequence(text: str):
    # Keras Tokenizer default: splits on characters here since
    # original char-level tokenization was used
    return [word_index.get(char, 0) for char in text]


def pad_sequence(seq, maxlen):
    seq = seq[:maxlen]
    padded = seq + [0] * (maxlen - len(seq))
    return padded

# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict(ciphertext: str):

    start = time.time()

    ciphertext = ciphertext.strip().replace(" ", "").lower()

    sequence = texts_to_sequence(ciphertext)
    padded = pad_sequence(sequence, MAX_LEN)
    padded = np.array([padded], dtype=np.float32)

    cipher_bytes = len(ciphertext) // 2
    key_length = cipher_bytes * 8
    cipher_length = cipher_bytes

    extra = np.array([[key_length, cipher_length]], dtype=np.float32)
    extra = np.repeat(extra[:, np.newaxis, :], MAX_LEN, axis=1)

    cnn_input = np.concatenate(
        [padded[..., np.newaxis], extra],
        axis=2
    ).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], cnn_input)
    interpreter.invoke()

    probabilities = interpreter.get_tensor(output_details[0]['index'])[0]

    best_index = int(np.argmax(probabilities))
    algorithm = label_classes[best_index]
    confidence = float(probabilities[best_index] * 100)

    top_indices = np.argsort(probabilities)[::-1][:3]

    top_predictions = []
    for idx in top_indices:
        top_predictions.append({
            "name": label_classes[int(idx)],
            "score": round(float(probabilities[idx] * 100), 2)
        })

    inference_time = round(time.time() - start, 4)

    return {
        "algorithm": algorithm,
        "confidence": round(confidence, 2),
        "top_predictions": top_predictions,
        "inference_time": inference_time
    }