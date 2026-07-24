from fastapi import FastAPI
import os

print("=" * 50)
print("Loaded API:", os.path.abspath(__file__))
print("=" * 50)
from pydantic import BaseModel

from tensorflow.keras.models import load_model

import pickle
import numpy as np

app = FastAPI()


# ----------------------------
# Load trained model
# ----------------------------

model = load_model("outputs/cnn_model.keras")

with open("outputs/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("outputs/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


MAX_LENGTH = 500


# ----------------------------
# Request Body
# ----------------------------

class CipherRequest(BaseModel):
    ciphertext: str


# ----------------------------
# Prediction Endpoint
# ----------------------------

@app.post("/predict")
def predict(data: CipherRequest):

    sequence = tokenizer.texts_to_sequences([data.ciphertext])

    padded = np.zeros((1, MAX_LENGTH))

    seq = sequence[0][:MAX_LENGTH]

    padded[0, :len(seq)] = seq

    prediction = model.predict(padded)

    class_index = np.argmax(prediction)

    algorithm = label_encoder.inverse_transform([class_index])[0]

    confidence = float(np.max(prediction))

    return {
        "algorithm": algorithm,
        "confidence": round(confidence * 100, 2)
    }