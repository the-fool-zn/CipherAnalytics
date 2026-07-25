export default function Footer() {
  return (
    <footer className="bg-slate-950 border-t border-slate-800 text-slate-400">
      <div className="mx-auto flex max-w-7xl flex-col items-center justify-between gap-4 px-6 py-8 md:flex-row">
        <div>
          <h3 className="text-lg font-semibold text-white">
            CipherAnalytics
          </h3>

          <p className="mt-2 text-sm">
            AI-Powered Cryptographic Algorithm Identification Platform.
          </p>
        </div>

        <p className="text-sm">
          © 2026 CipherAnalytics. Built with Next.js, FastAPI & TensorFlow.
        </p>
      </div>
    </footer>
  );
}