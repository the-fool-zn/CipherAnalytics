export default function Hero() {
  return (
    <section className="bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-28 lg:flex lg:items-center lg:justify-between">

        {/* Left Side */}
        <div className="max-w-3xl">

          <span className="rounded-full bg-blue-600/20 px-4 py-2 text-sm text-blue-400">
            AI-Powered Cryptography Analysis
          </span>

          <h1 className="mt-6 text-5xl font-extrabold leading-tight lg:text-6xl">
            Identify Cryptographic Algorithms
            <span className="block text-blue-500">
              using Artificial Intelligence
            </span>
          </h1>

          <p className="mt-8 text-lg text-slate-300 leading-8">
            CipherAnalytics uses Deep Learning to classify encrypted
            ciphertext into its originating cryptographic algorithm,
            enabling faster security analysis and research.
          </p>

          <div className="mt-10 flex gap-4">

            <button className="rounded-xl bg-blue-600 px-8 py-4 font-semibold hover:bg-blue-700 transition">
              Try Demo
            </button>

            <button className="rounded-xl border border-slate-700 px-8 py-4 hover:bg-slate-800 transition">
              Documentation
            </button>

          </div>

        </div>

        {/* Right Side */}

        <div className="mt-16 lg:mt-0">

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-2xl">

            <div className="font-mono text-green-400">

{`$ cipheranalytics predict

Uploading ciphertext...

Model Loaded ✔

Prediction:
AES-256

Confidence:
98.74%

Status:
Secure Encryption
`}

            </div>

          </div>

        </div>

      </div>
    </section>
  );
}