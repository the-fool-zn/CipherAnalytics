import os
import pickle
import joblib

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

# =====================================
# Configuration
# =====================================

DATASET_PATH = "dataset/cryptography_dataset_processed.csv"

MAX_SAMPLES = 10000

MAX_SEQUENCE_LENGTH = 512

TEST_SIZE = 0.15

VALIDATION_SIZE = 0.15

RANDOM_STATE = 42


# =====================================
# Load Dataset
# =====================================

def load_dataset():

    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    df = pd.read_csv(DATASET_PATH)

    print(f"\nDataset loaded successfully.")
    print(f"Shape: {df.shape}")

    required_columns = [
        "Algorithm",
        "Ciphertext",
        "Key Length (bits)",
        "Ciphertext Length (bytes)",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    print("\nAll required columns found.")

    return df

# =====================================
# Clean Dataset
# =====================================

def clean_dataset(df):

    print("\nCleaning dataset...")

    # Remove rows with missing values
    df = df.dropna()

    # Keep only required columns
    df = df[
        [
            "Algorithm",
            "Ciphertext",
            "Key Length (bits)",
            "Ciphertext Length (bytes)",
        ]
    ]

    # Convert ciphertext to string
    df["Ciphertext"] = df["Ciphertext"].astype(str)

    # Remove empty ciphertexts
    df = df[df["Ciphertext"].str.strip() != ""]

    # Optional sampling
    if MAX_SAMPLES is not None and MAX_SAMPLES < len(df):

        df = df.sample(
            n=MAX_SAMPLES,
            random_state=RANDOM_STATE
        )

        print(f"\nUsing sample size: {MAX_SAMPLES}")

    print(f"Clean dataset shape: {df.shape}")

    return df.reset_index(drop=True)

# =====================================
# Encode Labels
# =====================================

def encode_labels(df):

    print("\nEncoding labels...")

    label_encoder = LabelEncoder()

    labels = label_encoder.fit_transform(
        df["Algorithm"]
    )

    joblib.dump(label_encoder, "outputs/label_encoder.pkl")

    print(
        f"Found {len(label_encoder.classes_)} classes:"
    )

    for index, name in enumerate(label_encoder.classes_):
        print(f"{index}: {name}")

    return labels, label_encoder

# =====================================
# Tokenize Ciphertext
# =====================================

def tokenize_ciphertext(df):

    print("\nTokenizing ciphertext...")

    tokenizer = Tokenizer(
        char_level=True,
        lower=False
    )

    tokenizer.fit_on_texts(
        df["Ciphertext"]
    )

    sequences = tokenizer.texts_to_sequences(
        df["Ciphertext"]
    )

    padded_sequences = pad_sequences(
        sequences,
        maxlen=MAX_SEQUENCE_LENGTH,
        padding="post",
        truncating="post"
    )

    print(f"Vocabulary size: {len(tokenizer.word_index)}")
    print(f"Padded shape: {padded_sequences.shape}")

    return padded_sequences, tokenizer

# =====================================
# Prepare Numerical Features
# =====================================

def prepare_numeric_features(df):

    print("\nPreparing numerical features...")

    numeric_features = df[
        [
            "Key Length (bits)",
            "Ciphertext Length (bytes)",
        ]
    ].astype("float32").values

    print(
        f"Numeric feature shape: {numeric_features.shape}"
    )

    return numeric_features

# =====================================
# Split Dataset
# =====================================

def split_dataset(sequences, numeric_features, labels):

    print("\nSplitting dataset...")

    X_seq_train, X_seq_temp, X_num_train, X_num_temp, y_train, y_temp = train_test_split(
        sequences,
        numeric_features,
        labels,
        test_size=TEST_SIZE + VALIDATION_SIZE,
        random_state=RANDOM_STATE,
        stratify=labels
    )

    validation_ratio = VALIDATION_SIZE / (TEST_SIZE + VALIDATION_SIZE)

    X_seq_val, X_seq_test, X_num_val, X_num_test, y_val, y_test = train_test_split(
        X_seq_temp,
        X_num_temp,
        y_temp,
        test_size=validation_ratio,
        random_state=RANDOM_STATE,
        stratify=y_temp
    )

    print(f"\nTraining samples:   {len(y_train)}")
    print(f"Validation samples: {len(y_val)}")
    print(f"Testing samples:    {len(y_test)}")

    return (
        X_seq_train,
        X_seq_val,
        X_seq_test,
        X_num_train,
        X_num_val,
        X_num_test,
        y_train,
        y_val,
        y_test,
    )

# =====================================
# Create CNN Input Tensor
# =====================================

def create_cnn_inputs(
    X_sequences,
    numeric_features,
):

    print("\nCreating CNN input tensor...")

    repeated_features = np.repeat(
        numeric_features[:, np.newaxis, :],
        MAX_SEQUENCE_LENGTH,
        axis=1,
    )

    cnn_input = np.concatenate(
        [
            X_sequences[..., np.newaxis],
            repeated_features,
        ],
        axis=2,
    )

    print("CNN Input Shape:", cnn_input.shape)

    return cnn_input

# =====================================
# Convert Labels
# =====================================

def convert_labels(
    y_train,
    y_val,
    y_test,
    num_classes,
):

    print("\nConverting labels to categorical...")

    y_train = to_categorical(
        y_train,
        num_classes,
    )

    y_val = to_categorical(
        y_val,
        num_classes,
    )

    y_test = to_categorical(
        y_test,
        num_classes,
    )

    print("Training Labels:", y_train.shape)
    print("Validation Labels:", y_val.shape)
    print("Testing Labels:", y_test.shape)

    return (
        y_train,
        y_val,
        y_test,
    )

# =====================================
# Save Training Data
# =====================================

def save_training_data(
    X_train,
    X_val,
    X_test,
    y_train,
    y_val,
    y_test,
):

    print("\nSaving processed datasets...")

    os.makedirs("outputs", exist_ok=True)

    np.save(
        "outputs/X_train.npy",
        X_train,
    )

    np.save(
        "outputs/X_val.npy",
        X_val,
    )

    np.save(
        "outputs/X_test.npy",
        X_test,
    )

    np.save(
        "outputs/y_train.npy",
        y_train,
    )

    np.save(
        "outputs/y_val.npy",
        y_val,
    )

    np.save(
        "outputs/y_test.npy",
        y_test,
    )

    print("Datasets saved successfully.")

# =====================================
# Save Preprocessing Objects
# =====================================

def save_preprocessors(tokenizer, label_encoder):

    print("\nSaving preprocessing objects...")

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/tokenizer.pkl", "wb") as file:
        pickle.dump(tokenizer, file)

    with open("outputs/label_encoder.pkl", "wb") as file:
        pickle.dump(label_encoder, file)

    print("Tokenizer saved.")
    print("Label encoder saved.")

# =====================================
# Main
# =====================================

if __name__ == "__main__":

    dataframe = load_dataset()

    dataframe = clean_dataset(dataframe)

    labels, label_encoder = encode_labels(dataframe)

    sequences, tokenizer = tokenize_ciphertext(dataframe)

    numeric_features = prepare_numeric_features(dataframe)

    (
    X_seq_train,
    X_seq_val,
    X_seq_test,
    X_num_train,
    X_num_val,
    X_num_test,
    y_train,
    y_val,
    y_test,
) = split_dataset(
    sequences,
    numeric_features,
    labels,
)

X_train_final = create_cnn_inputs(
    X_seq_train,
    X_num_train,
)

X_val_final = create_cnn_inputs(
    X_seq_val,
    X_num_val,
)

X_test_final = create_cnn_inputs(
    X_seq_test,
    X_num_test,
)

num_classes = len(label_encoder.classes_)

(
    y_train,
    y_val,
    y_test,
) = convert_labels(
    y_train,
    y_val,
    y_test,
    num_classes,
)

save_training_data(
    X_train_final,
    X_val_final,
    X_test_final,
    y_train,
    y_val,
    y_test,
)

save_preprocessors(
    tokenizer,
    label_encoder,
)

print("\nFirst five rows:")
print(dataframe.head())