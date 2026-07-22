const algorithms = [
  "AES",
  "DES",
  "3DES",
  "Blowfish",
  "RSA",
  "ChaCha20",
  "RC4",
  "ECC",
];

export default function SupportedAlgorithms() {
  return (
    <section className="bg-slate-900 text-white py-24">
      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">
          <h2 className="text-4xl font-bold">
            Supported Algorithms
          </h2>

          <p className="mt-4 max-w-2xl mx-auto text-slate-400">
            CipherAnalytics is designed to recognize a wide range of modern
            and legacy cryptographic algorithms using AI-driven pattern analysis.
          </p>
        </div>

        <div className="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          {algorithms.map((algorithm) => (
            <div
              key={algorithm}
              className="rounded-xl border border-slate-700 bg-slate-800 p-6 text-center text-lg font-semibold hover:border-blue-500 hover:bg-slate-700 transition"
            >
              {algorithm}
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}