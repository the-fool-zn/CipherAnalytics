"use client";

import { useState } from "react";

import UploadBox from "@/components/prediction/UploadBox";
import PredictionCard from "@/components/prediction/PredictionCard";
import TopPredictions from "@/components/prediction/TopPredictions";
import LoadingState from "@/components/prediction/LoadingState";


type PredictionResult = {
  algorithm: string;
  confidence: number;
  inferenceTime: number;

  topPredictions: {
    name: string;
    score: number;
  }[];
};


export default function PredictPage() {

  const [prediction, setPrediction] =
    useState<PredictionResult | null>(null);

  const [loading, setLoading] =
    useState(false);


  return (
    <main className="min-h-screen bg-slate-950 text-white">

      <div className="mx-auto max-w-5xl px-6 py-20">

        <h1 className="text-5xl font-bold">
          Ciphertext Prediction
        </h1>


        <p className="mt-4 text-slate-400">
          Upload or paste encrypted ciphertext to identify
          the cryptographic algorithm using our AI model.
        </p>


        <div className="mt-12">

          <UploadBox
            onPrediction={setPrediction}
            setLoading={setLoading}
          />

        </div>


        {loading && (
          <div className="mt-10">
            <LoadingState />
          </div>
        )}


        {prediction && !loading && (
          <div className="mt-10 space-y-6">

            <PredictionCard
              algorithm={prediction.algorithm}
              confidence={prediction.confidence}
              inferenceTime={prediction.inferenceTime}
            />


            <TopPredictions
              predictions={prediction.topPredictions}
            />

          </div>
        )}


      </div>

    </main>
  );
}