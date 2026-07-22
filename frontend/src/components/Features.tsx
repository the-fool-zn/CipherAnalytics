const features = [
  {
    title: "AI Classification",
    description:
      "Deep learning models identify cryptographic algorithms directly from ciphertext.",
  },
  {
    title: "Fast Predictions",
    description:
      "Receive algorithm predictions in seconds using an optimized inference pipeline.",
  },
  {
    title: "Confidence Scores",
    description:
      "Every prediction includes confidence values for transparent decision-making.",
  },
  {
    title: "Multiple Algorithms",
    description:
      "Support for AES, DES, Blowfish, RSA, ChaCha20 and more.",
  },
  {
    title: "Secure Processing",
    description:
      "Ciphertext is processed securely without exposing sensitive information.",
  },
  {
    title: "Research Ready",
    description:
      "Designed for researchers, students, and cybersecurity professionals.",
  },
];

export default function Features() {
  return (
    <section className="bg-slate-900 text-white py-24">
      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">
          <h2 className="text-4xl font-bold">
            Why Choose CipherAnalytics?
          </h2>

          <p className="mt-4 text-slate-400 max-w-2xl mx-auto">
            A modern AI-powered platform for cryptographic algorithm
            identification, built for speed, accuracy, and research.
          </p>
        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="rounded-2xl border border-slate-700 bg-slate-800 p-8 hover:border-blue-500 hover:shadow-lg transition"
            >
              <h3 className="text-xl font-semibold text-blue-400">
                {feature.title}
              </h3>

              <p className="mt-4 text-slate-300">
                {feature.description}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}