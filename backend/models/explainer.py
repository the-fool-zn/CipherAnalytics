import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """
You are a cryptography tutor embedded in an app called CipherAnalytics.

A machine learning model has predicted which encryption algorithm produced a piece of ciphertext.

Given the predicted algorithm and confidence score, explain the result to a beginner.

Rules:
- Respond in 2–4 sentences.
- No headings.
- No bullet points.
- Explain whether the algorithm is symmetric/asymmetric and block/stream when appropriate.
- Mention one common real-world use.
- If confidence is below 60%, mention that the prediction may be uncertain.
- Do not repeat the exact confidence number.
"""


def explain_prediction(algorithm: str, confidence: float) -> str:

    if not OPENROUTER_API_KEY:
        return "OpenRouter API key not configured."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-oss-20b:free",
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": (
                    f"Predicted algorithm: {algorithm}\n"
                    f"Confidence: {confidence}"
                ),
            },
        ],
        "temperature": 0.5,
        "max_tokens": 300,
        "reasoning": {
            "effort": "low"
        },
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30,
        )

        if response.status_code != 200:
            print("OpenRouter Error:")
            print(response.status_code)
            print(response.text)
            return "Explanation unavailable right now."

        data = response.json()

        message = data["choices"][0]["message"]

        # Normal response
        content = message.get("content")

        # Fallback for reasoning models
        if not content:
            content = message.get("reasoning")

        if content:
            return content.strip()

        return "Explanation unavailable."

    except Exception as e:
        print("OPENROUTER ERROR:", e)
        return "Explanation unavailable right now."