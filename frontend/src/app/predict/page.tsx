import UploadBox from "@/components/prediction/UploadBox";
import PredictionCard from "@/components/prediction/PredictionCard";

export default function PredictPage() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-5xl px-6 py-20">
        <h1 className="text-5xl font-bold">
          Ciphertext Prediction
        </h1>

        <p className="mt-4 text-slate-400">
          Upload or paste encrypted ciphertext to identify the
          cryptographic algorithm using our AI model.
        </p>

        <div className="mt-12">
          <UploadBox />
        </div>

        <div className="mt-10">
          <PredictionCard
            algorithm="AES-256"
            confidence={98.74}
            inferenceTime={0.14}
          />
        </div>
      </div>
    </main>
  );
}