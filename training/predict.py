import pickle
import joblib
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ==========================
# Load model
# ==========================

model = load_model("outputs/cnn_model.keras")

# ==========================
# Load tokenizer
# ==========================

with open("outputs/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# ==========================
# Load label encoder
# ==========================

label_encoder = joblib.load("outputs/label_encoder.pkl")

# ==========================
# User Input
# ==========================

ciphertext = input("Enter ciphertext: ")

key_length = float(input("Key length (bits): "))

cipher_length = float(input("Ciphertext length (bytes): "))

# ==========================
# Preprocess ciphertext
# ==========================

sequence = tokenizer.texts_to_sequences([ciphertext])

sequence = pad_sequences(
    sequence,
    maxlen=512,
    padding="post",
    truncating="post",
)

numeric = np.array([[key_length, cipher_length]])

numeric = np.repeat(
    numeric[:, np.newaxis, :],
    512,
    axis=1,
)

cnn_input = np.concatenate(
    [
        sequence[..., np.newaxis],
        numeric,
    ],
    axis=2,
)

# ==========================
# Predict
# ==========================

prediction = model.predict(cnn_input, verbose=0)[0]

# Get top 3 predictions
top3_indices = np.argsort(prediction)[::-1][:3]

print("\nTop 3 Predictions")
print("----------------------")

for rank, index in enumerate(top3_indices, start=1):

    algorithm = label_encoder.inverse_transform([index])[0]

    confidence = prediction[index] * 100

    print(f"{rank}. {algorithm:<15} {confidence:.2f}%")