type PredictionCardProps = {
  algorithm: string;
  confidence: number;
  inferenceTime: number;
};

export default function PredictionCard({
  algorithm,
  confidence,
  inferenceTime,
}: PredictionCardProps) {
  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-8">
      <h2 className="text-2xl font-bold text-blue-400">
        Prediction Result
      </h2>

      <div className="mt-8 space-y-4">
        <div className="flex justify-between">
          <span>Algorithm</span>
          <span className="font-semibold">{algorithm}</span>
        </div>

        <div className="flex justify-between">
          <span>Confidence</span>
          <span>{confidence}%</span>
        </div>

        <div className="flex justify-between">
          <span>Inference Time</span>
          <span>{inferenceTime}s</span>
        </div>
      </div>
    </div>
  );
}