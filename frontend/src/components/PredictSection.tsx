"use client";

import { useState, useRef, useEffect } from "react";

import UploadBox from "./prediction/UploadBox";
import PredictionCard from "./prediction/PredictionCard";
import PredictionHistory from "./prediction/PredictionHistory";
import LoadingState from "./prediction/LoadingState";

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

export default function PredictSection() {
  const [loading, setLoading] = useState(false);

  const [result, setResult] =
    useState<PredictionResult | null>(null);

  const [history, setHistory] = useState<PredictionResult[]>([]);

  const resultRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (result && resultRef.current) {
      resultRef.current.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  }, [result]);

  return (
    <section
      id="predict"
      className="bg-slate-950 py-20"
    >
      <div className="mx-auto max-w-7xl px-6">

        <h2 className="mb-12 text-center text-4xl font-bold text-white">
          Live Cipher Prediction
        </h2>

        <div className="grid gap-10 lg:grid-cols-2">

          <UploadBox
            onPrediction={(prediction) => {
              setResult(prediction);
              setHistory((prev) => [
                prediction,
                ...prev.slice(0, 4),
              ]);
            }}
            setLoading={setLoading}
          />

          <div ref={resultRef}>

            {loading && <LoadingState />}

            {!loading && result && (
              <>
                <PredictionCard
                  algorithm={result.algorithm}
                  confidence={result.confidence}
                  inferenceTime={result.inferenceTime}
                  topPredictions={result.topPredictions}
                  explanation={result.explanation}
                />

                <PredictionHistory
                  history={history}
                />
              </>
            )}

          </div>

        </div>

      </div>
    </section>
  );
}