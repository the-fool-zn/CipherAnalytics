type Props = {
  confidence: number;
};


export default function ConfidenceBar({
  confidence,
}: Props) {

  return (
    <div className="mt-6">

      <div className="mb-2 flex justify-between text-sm">
        <span>
          Confidence Score
        </span>

        <span>
          {confidence}%
        </span>
      </div>


      <div className="h-3 w-full rounded-full bg-slate-700">

        <div
          className="h-3 rounded-full bg-blue-500 transition-all"
          style={{
            width: `${confidence}%`,
          }}
        />

      </div>

    </div>
  );
}