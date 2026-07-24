import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a cryptography tutor embedded in an app called CipherAnalytics.
A machine learning model has just predicted which encryption algorithm produced a piece of ciphertext.
Given the predicted algorithm name and the model's confidence score, write a short, clear explanation for a student who may not know cryptography.

Your response must:
- Be 2-4 sentences, plain language, no headers or bullet points.
- Briefly explain what the predicted algorithm is (symmetric/asymmetric, block/stream, etc).
- Mention one real-world use case of that algorithm.
- If confidence is below 60, add a short caveat that the prediction is uncertain.

Do not repeat the raw confidence number back verbatim; describe it qualitatively (e.g. "high confidence", "somewhat uncertain")."""


def explain_prediction(algorithm: str, confidence: float) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Predicted algorithm: {algorithm}\nConfidence: {confidence}"}
            ],
            max_tokens=200,
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Explanation unavailable right now."