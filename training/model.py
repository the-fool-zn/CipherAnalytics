from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv1D,
    MaxPooling1D,
    GlobalAveragePooling1D,
    Dense,
    Dropout,
)

from tensorflow.keras.optimizers import Adam


# =====================================
# Build CNN Model
# =====================================

def build_model(input_shape, num_classes):

    model = Sequential([

    # First Convolution Block
    Conv1D(
        filters=64,
        kernel_size=5,
        activation="relu",
        input_shape=input_shape,
    ),

    MaxPooling1D(pool_size=2),

    # Second Block
    Conv1D(
        filters=128,
        kernel_size=3,
        activation="relu",
    ),

    MaxPooling1D(pool_size=2),

    # Global Pooling
    GlobalAveragePooling1D(),

    # Dense Layer
    Dense(
        128,
        activation="relu",
    ),

    Dropout(0.3),

    # Output
    Dense(
        num_classes,
        activation="softmax",
    ),

])

    model.compile(

        optimizer=Adam(),

        loss="categorical_crossentropy",

        metrics=["accuracy"],
    )

    return model