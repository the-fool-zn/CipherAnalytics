from datetime import datetime
import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from models.predictor import predict
from models.explainer import explain_prediction
from utils.validator import validate_ciphertext


router = APIRouter()


class CipherRequest(BaseModel):
    ciphertext: str


@router.post("/predict")
def predict_cipher(request: CipherRequest):

    # Validate the input before sending it to the AI model
    valid, message = validate_ciphertext(request.ciphertext)

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    # Run AI prediction
    result = predict(request.ciphertext)

    # Generate AI explanation
    result["explanation"] = explain_prediction(
        result["algorithm"],
        result["confidence"]
    )

    # Generate unique prediction ID
    result["prediction_id"] = (
        "CA-"
        + datetime.now().strftime("%Y%m%d")
        + "-"
        + uuid.uuid4().hex[:6].upper()
    )

    # Add analysis timestamp
    result["timestamp"] = datetime.now().isoformat()

    return result