# CipherAnalytics

**AI-powered cryptographic algorithm identification platform**

CipherAnalytics uses a deep learning model to analyze ciphertext and predict which cryptographic algorithm was used to produce it — then uses a large language model to explain the result in plain language.

## The Problem

Identifying which encryption algorithm produced a piece of ciphertext is normally something only an experienced cryptography practitioner can do by eye — by recognizing block sizes, encoding patterns, and structural clues. This is a real barrier for:

- **Cybersecurity students and researchers**, who are learning to recognize cryptographic patterns and need a fast way to check their own analysis
- **Security professionals**, who occasionally need a quick, preliminary read on an unfamiliar ciphertext sample without manually running it through multiple tools

CipherAnalytics solves this by pairing a trained CNN classifier with an AI explanation layer, so a user can paste in ciphertext and get both a prediction *and* a plain-language explanation of what that algorithm is and why the model thinks so — in seconds, for free.

## Live Demo

**🔗 [https://cipher-analytics-2qgm.vercel.app](https://cipher-analytics-2qgm.vercel.app)**

Backend API: [https://cipheranalytics-api.onrender.com](https://cipheranalytics-api.onrender.com)

> Note: the backend runs on Render's free tier, which spins down after periods of inactivity. If the app has been idle, the first prediction may take 30–60 seconds while the server wakes up — this is expected, not a bug.

## Features

- **Paste or upload ciphertext** — type directly into the app, or upload a `.txt` file
- **AI algorithm classification** — a trained convolutional neural network (CNN) predicts the cryptographic algorithm from the ciphertext, with a confidence score and top-3 alternative predictions
- **AI-generated explanation** — a large language model explains the predicted algorithm in plain language: whether it's symmetric/asymmetric, block/stream, and a real-world use case, tailored to the specific prediction and confidence level
- **Ciphertext statistics panel** — length, estimated byte size, detected character set (hex/Base64/mixed), and input validity
- **Confidence badge** — color-coded (🟢 high / 🟡 medium / 🔴 low) for at-a-glance interpretation
- **Input validation** — rejects ciphertext that's too short or has unsupported characters before sending it to the model
- **Prediction history** — the last 5 predictions in the current session, viewable at a glance
- **Downloadable PDF report** — a formatted report of any prediction, including the explanation and top predictions, generated client-side
- **Copy result to clipboard** — one-click copy of the prediction summary
- **Responsive, modern UI** — built with Next.js and Tailwind CSS

## The AI Feature

CipherAnalytics uses two AI components working together:

### Model Notes

The CNN classifier was trained on a labeled cryptography dataset from Kaggle. It demonstrates the full pipeline—preprocessing, training, inference, and deployment—while AI explanations are generated using OpenRouter's free LLM API. Since free LLMs do not support ciphertext recognition and public datasets are limited, prediction accuracy remains constrained. CipherAnalytics is a working proof-of-concept for AI-assisted cipher identification and will continue to be improved with more capable models and datasets.

**1. A trained CNN classifier** (TensorFlow/Keras, converted to TensorFlow Lite for deployment) predicts the cryptographic algorithm from the ciphertext's character sequence and numerical features (key length, ciphertext length). Trained on a labeled cryptography dataset covering AES, DES, Triple DES, Blowfish, RC4, ChaCha20, RSA, and ECC.

**2. An LLM explanation layer**, called via [OpenRouter](https://openrouter.ai), takes the CNN's prediction (algorithm + confidence) and generates a short, plain-language explanation for the user. This is the system prompt used:

```
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
```

The model used is `openai/gpt-oss-20b:free` via OpenRouter's free tier.

## Tools, Services & Models Used

| Component | Technology |
|---|---|
| Frontend framework | Next.js (React) + TypeScript |
| Styling | Tailwind CSS |
| Backend framework | FastAPI (Python) |
| ML model | TensorFlow / Keras CNN, converted to TensorFlow Lite (`ai-edge-litert`) for lightweight inference |
| AI explanation model | `openai/gpt-oss-20b:free` via OpenRouter |
| PDF generation | jsPDF (client-side) |
| Frontend hosting | Vercel |
| Backend hosting | Render (free tier) |
| Version control | Git / GitHub |
| Notifications | react-hot-toast |

## Architecture

```text
User
   │
   ▼
Next.js Frontend
   │
   ▼
FastAPI Backend
   ├────────► TensorFlow Lite CNN
   │
   └────────► OpenRouter LLM
                   │
                   ▼
            Explanation
```

## Screenshots

**1. Homepage — Hero section**

<img width="1920" height="1080" alt="Home Page" src="https://github.com/user-attachments/assets/0a683447-74f6-48bf-bca7-46d035f46c17" />


**2. How It Works & Supported Algorithms**

<img width="1920" height="1080" alt="How it works" src="https://github.com/user-attachments/assets/df1b15db-3d8a-4540-84bf-b881001c1025" />


**3. Live prediction with AI explanation, top predictions, and ciphertext statistics**

<img width="1920" height="1080" alt="Predictions" src="https://github.com/user-attachments/assets/1a903ff4-34bd-4cd9-a6e4-083d8d17702f" />


## How to Run Locally

### Prerequisites
- Node.js 18+
- Python 3.12
- An OpenRouter API key ([get one free here](https://openrouter.ai))

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt

# Create a .env file or set environment variables:
# OPENROUTER_API_KEY=your_key_here

uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install

# Create frontend/.env.local with:
# NEXT_PUBLIC_API_URL=http://localhost:8000

npm run dev
```

Frontend runs at `http://localhost:3000`.

## Project Structure

```
CipherAnalytics/
├── backend/
│   ├── main.py                 # FastAPI app entrypoint
│   ├── routes/predict.py       # /api/predict endpoint
│   ├── models/
│   │   ├── predictor.py        # CNN model inference (TFLite)
│   │   └── explainer.py        # AI explanation via OpenRouter
│   ├── utils/validator.py      # Ciphertext input validation
│   ├── ai/                     # Trained model + tokenizer artifacts
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/                # Next.js app router pages
│   │   └── components/         # UI components (prediction UI, landing page sections)
│   └── package.json
└── training/                   # Model training pipeline (preprocessing, training scripts)
```

## Future Work

- Train on larger and more diverse cryptographic datasets
- Improve classification accuracy using transformer-based models
- Support additional encryption algorithms
- Add batch ciphertext analysis
- Compare predictions from multiple AI models

## Author

Built by **Muhammad Zain Nasir**

GitHub: **[@the-fool-zn](https://github.com/the-fool-zn)**
