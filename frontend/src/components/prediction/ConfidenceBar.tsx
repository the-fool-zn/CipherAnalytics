type Props = {
  confidence: number;
};

export default function ConfidenceBar({
  confidence,
}: Props) {
  let label = "";
  let color = "";

  if (confidence >= 90) {
    label = "🟢 Very High Confidence";
    color = "bg-emerald-500";
  } else if (confidence >= 75) {
    label = "🟢 High Confidence";
    color = "bg-green-500";
  } else if (confidence >= 60) {
    label = "🟡 Moderate Confidence";
    color = "bg-yellow-500";
  } else {
    label = "🔴 Low Confidence";
    color = "bg-red-500";
  }

  return (
    <div className="mt-6">
      <div className="mb-2 flex justify-between text-sm">
        <span className="font-medium">{label}</span>

        <span className="font-semibold">
          {confidence.toFixed(2)}%
        </span>
      </div>

      <div className="h-3 w-full rounded-full bg-slate-700">
        <div
          className={`h-3 rounded-full transition-all ${color}`}
          style={{
            width: `${confidence}%`,
          }}
        />
      </div>
    </div>
  );
}