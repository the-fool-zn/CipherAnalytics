export default function LoadingState() {
  return (
    <div className="mt-8 rounded-2xl border border-slate-700 bg-slate-900 p-8 text-center">

      <div className="text-xl font-semibold text-blue-400">
        Analyzing Ciphertext...
      </div>

      <div className="mt-6 space-y-3 text-slate-300">

        <p>
          ◉ Processing encrypted input
        </p>

        <p>
          ◉ Extracting cryptographic patterns
        </p>

        <p>
          ◉ Running AI classifier
        </p>

        <p>
          ◉ Generating prediction
        </p>

      </div>

    </div>
  );
}