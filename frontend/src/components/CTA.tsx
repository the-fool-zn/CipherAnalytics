export default function CTA() {
  return (
    <section className="bg-blue-600 text-white py-20">
      <div className="mx-auto max-w-4xl px-6 text-center">
        <h2 className="text-4xl font-bold">
          Ready to Analyze Your Ciphertext?
        </h2>

        <p className="mt-6 text-lg text-blue-100">
          Upload encrypted ciphertext and let our AI identify the underlying
          cryptographic algorithm in seconds.
        </p>

        <button className="mt-10 rounded-xl bg-white px-8 py-4 font-semibold text-blue-700 transition hover:bg-slate-100">
          Start Prediction
        </button>
      </div>
    </section>
  );
}