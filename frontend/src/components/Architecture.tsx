const architecture = [
  {
    title: "Next.js Frontend",
    description: "Modern React interface for uploading ciphertext and displaying predictions.",
  },
  {
    title: "FastAPI Backend",
    description: "Handles API requests, validation, preprocessing, and communication with the AI model.",
  },
  {
    title: "PyTorch AI Model",
    description: "Processes ciphertext and predicts the most likely cryptographic algorithm.",
  },
  {
    title: "Prediction Results",
    description: "Returns the predicted algorithm, confidence score, and inference details.",
  },
];

export default function Architecture() {
  return (
    <section className="bg-slate-950 text-white py-24">
      <div className="mx-auto max-w-7xl px-6">
        <div className="text-center">
          <h2 className="text-4xl font-bold">
            Platform Architecture
          </h2>

          <p className="mt-4 max-w-2xl mx-auto text-slate-400">
            CipherAnalytics follows a modern AI application architecture,
            separating the user interface, backend services, and machine learning model.
          </p>
        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-4">
          {architecture.map((item) => (
            <div
              key={item.title}
              className="rounded-2xl border border-slate-700 bg-slate-900 p-6 hover:border-blue-500 transition"
            >
              <h3 className="text-xl font-semibold text-blue-400">
                {item.title}
              </h3>

              <p className="mt-4 text-slate-300">
                {item.description}
              </p>
            </div>
          ))}
        </div>

        <div className="mt-12 text-center text-blue-400 font-mono text-lg">
          Next.js → FastAPI → PyTorch → Prediction
        </div>
      </div>
    </section>
  );
}