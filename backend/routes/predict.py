from fastapi import APIRouter
from pydantic import BaseModel

from models.predictor import predict
from models.explainer import explain_prediction


router = APIRouter()


class CipherRequest(BaseModel):
    ciphertext: str


@router.post("/predict")
def predict_cipher(request: CipherRequest):

    result = predict(request.ciphertext)

    result["explanation"] = explain_prediction(
        result["algorithm"],
        result["confidence"]
    )

    return result