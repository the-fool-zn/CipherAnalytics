import os
import numpy as np

from tensorflow.keras.callbacks import EarlyStopping

from model import build_model


# =====================================
# Load Data
# =====================================

print("\nLoading processed datasets...")

X_train = np.load("outputs/X_train.npy")
X_val = np.load("outputs/X_val.npy")
X_test = np.load("outputs/X_test.npy")

y_train = np.load("outputs/y_train.npy")
y_val = np.load("outputs/y_val.npy")
y_test = np.load("outputs/y_test.npy")

print("Training:", X_train.shape)
print("Validation:", X_val.shape)
print("Testing:", X_test.shape)


# =====================================
# Build Model
# =====================================

print("\nBuilding CNN...")

model = build_model(

    input_shape=X_train.shape[1:],

    num_classes=y_train.shape[1],

)

model.summary()


# =====================================
# Early Stopping
# =====================================

early_stop = EarlyStopping(

    monitor="val_accuracy",

    patience=3,

    restore_best_weights=True,

)


# =====================================
# Train Model
# =====================================

print("\nTraining CNN...\n")

history = model.fit(

    X_train,

    y_train,

    validation_data=(

        X_val,

        y_val,

    ),

    epochs=20,

    batch_size=64,

    callbacks=[early_stop],

)


# =====================================
# Evaluate
# =====================================

print("\nEvaluating model...\n")

loss, accuracy = model.evaluate(

    X_test,

    y_test,

    verbose=1,

)

print(f"\nTest Accuracy: {accuracy:.4f}")


# =====================================
# Save Model
# =====================================

os.makedirs("outputs", exist_ok=True)

model.save("outputs/cnn_model.keras")

print("\nModel saved successfully!")

print("\nLocation:")

print("outputs/cnn_model.keras")