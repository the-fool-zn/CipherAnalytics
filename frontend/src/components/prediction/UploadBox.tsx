"use client";

import { useState } from "react";
import { Loader2 } from "lucide-react";

type PredictionResult = {
  algorithm: string;
  confidence: number;
  inferenceTime: number;
  topPredictions: {
    name: string;
    score: number;
  }[];
  explanation: string;
};

type UploadBoxProps = {
  onPrediction: (result: PredictionResult) => void;
  setLoading: (value: boolean) => void;
};

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function UploadBox({
  onPrediction,
  setLoading,
}: UploadBoxProps) {
  const [ciphertext, setCiphertext] = useState("");
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [fileName, setFileName] = useState("");

  const handlePredict = async () => {
    if (!ciphertext.trim()) {
      alert("Please enter ciphertext first.");
      return;
    }

    setLoading(true);
    setIsAnalyzing(true);

    try {
      const response = await fetch(
        `${API_URL}/api/predict`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ciphertext,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Prediction request failed");
      }

      const data = await response.json();

      onPrediction({
        algorithm: data.algorithm,
        confidence: data.confidence,
        inferenceTime: data.inference_time,
        topPredictions: data.top_predictions,
        explanation: data.explanation,
      });
    } catch (error) {
      console.error(error);
      alert("Unable to connect to CipherAnalytics API.");
    } finally {
      setLoading(false);
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-8">

      <label
        htmlFor="ciphertext"
        className="mb-3 block text-lg font-semibold text-white"
      >
        Paste Ciphertext
      </label>

      <textarea
        id="ciphertext"
        rows={10}
        value={ciphertext}
        onChange={(e) => setCiphertext(e.target.value)}
        placeholder="Paste encrypted ciphertext here..."
        className="w-full rounded-xl border border-slate-700 bg-slate-950 p-4 text-white outline-none focus:border-blue-500"
      />

      <div className="mt-6">

        <label
          htmlFor="cipherFile"
          className="mb-2 block font-medium text-white"
        >
          Or Upload a .txt File
        </label>

        <input
          id="cipherFile"
          type="file"
          accept=".txt"
          onChange={async (e) => {
            const file = e.target.files?.[0];

            if (!file) return;

            try {
              const text = await file.text();

              setCiphertext(text.trim());
              setFileName(file.name);

            } catch (err) {
              console.error(err);
              alert("Unable to read the selected file.");
            }
          }}
          className="block w-full rounded-lg border border-slate-700 bg-slate-950 p-3 text-white
          file:mr-4 file:rounded-lg file:border-0
          file:bg-blue-600 file:px-4 file:py-2
          file:text-white hover:file:bg-blue-700"
        />

        {fileName && (
          <p className="mt-3 text-sm text-green-400">
            ✔ Loaded: {fileName}
          </p>
        )}

      </div>

            <div className="mt-8 flex gap-4">

        <button
          onClick={handlePredict}
          disabled={isAnalyzing}
          className="flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-8 py-4 font-semibold text-white transition hover:bg-blue-700 disabled:opacity-50"
        >
          {isAnalyzing ? (
            <>
              <Loader2 className="h-5 w-5 animate-spin" />
              Analyzing...
            </>
          ) : (
            "Predict Algorithm"
          )}
        </button>

        <button
          type="button"
          onClick={() => {
            setCiphertext("");
            setFileName("");
          }}
          className="rounded-xl border border-slate-600 px-8 py-4 font-semibold text-white transition hover:bg-slate-800"
        >
          Clear
        </button>

      </div>

    </div>
  );
}