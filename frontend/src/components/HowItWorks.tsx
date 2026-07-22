const steps = [
  {
    number: "01",
    title: "Upload Ciphertext",
    description:
      "Upload or paste encrypted ciphertext into the platform for analysis.",
  },
  {
    number: "02",
    title: "AI Model Analysis",
    description:
      "Our trained deep learning model extracts patterns and identifies the encryption algorithm.",
  },
  {
    number: "03",
    title: "Prediction Results",
    description:
      "Receive the predicted algorithm along with confidence scores and detailed insights.",
  },
];

export default function HowItWorks() {
  return (
    <section className="bg-slate-950 text-white py-24">
      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">
          <h2 className="text-4xl font-bold">
            How It Works
          </h2>

          <p className="mt-4 max-w-2xl mx-auto text-slate-400">
            CipherAnalytics makes cryptographic algorithm identification simple
            through an AI-powered three-step workflow.
          </p>
        </div>

        <div className="mt-20 grid gap-10 md:grid-cols-3">

          {steps.map((step) => (
            <div
              key={step.number}
              className="rounded-2xl border border-slate-700 bg-slate-900 p-8 text-center hover:border-blue-500 transition"
            >
              <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-blue-600 text-2xl font-bold">
                {step.number}
              </div>

              <h3 className="mt-6 text-2xl font-semibold">
                {step.title}
              </h3>

              <p className="mt-4 text-slate-300 leading-7">
                {step.description}
              </p>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
}