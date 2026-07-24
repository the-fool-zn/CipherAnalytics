type Prediction = {
  algorithm: string;
  confidence: number;
  inferenceTime: number;
};

type Props = {
  history: Prediction[];
};

export default function PredictionHistory({
  history,
}: Props) {
  if (history.length === 0) return null;

  return (
    <div className="mt-8 rounded-2xl border border-slate-700 bg-slate-900 p-6 shadow-xl">

      <h3 className="mb-6 text-xl font-bold text-blue-400">
        Recent Predictions
      </h3>

      <div className="overflow-x-auto">

        <table className="w-full text-left">

          <thead>

            <tr className="border-b border-slate-700 text-slate-400">

              <th className="pb-3">#</th>

              <th className="pb-3">Algorithm</th>

              <th className="pb-3">Confidence</th>

              <th className="pb-3">Time</th>

            </tr>

          </thead>

          <tbody>

            {history.map((item, index) => (

              <tr
                key={index}
                className="border-b border-slate-800"
              >

                <td className="py-3 text-white">
                  {index + 1}
                </td>

                <td className="py-3 font-semibold text-white">
                  {item.algorithm}
                </td>

                <td className="py-3 text-green-400">
                  {item.confidence.toFixed(2)}%
                </td>

                <td className="py-3 text-slate-300">
                  {item.inferenceTime.toFixed(4)} s
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}