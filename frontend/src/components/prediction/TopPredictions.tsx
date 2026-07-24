type Props = {
  predictions: {
    name: string;
    score: number;
  }[];
};

export default function TopPredictions({
  predictions,
}: Props) {
  return (
    <div className="mt-8 rounded-2xl border border-slate-700 bg-slate-800 p-6">

      <h3 className="text-xl font-bold text-blue-400">
        Top Predictions
      </h3>

      <div className="mt-5 space-y-4">

        {predictions.map((item, index) => (

          <div
            key={item.name}
            className="flex items-center justify-between border-b border-slate-700 pb-3 last:border-none"
          >

            <div className="flex items-center gap-3">

              <span className="flex h-8 w-8 items-center justify-center rounded-full bg-blue-600 text-sm font-bold text-white">
                {index + 1}
              </span>

              <span className="font-medium text-white">
                {item.name}
              </span>

            </div>

            <span className="font-semibold text-green-400">
              {item.score.toFixed(2)}%
            </span>

          </div>

        ))}

      </div>

    </div>
  );
}