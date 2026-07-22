export default function UploadBox() {
  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-8">
      <label
        htmlFor="ciphertext"
        className="mb-3 block text-lg font-semibold"
      >
        Paste Ciphertext
      </label>

      <textarea
        id="ciphertext"
        rows={10}
        placeholder="Paste encrypted ciphertext here..."
        className="w-full rounded-xl border border-slate-700 bg-slate-950 p-4 text-white outline-none focus:border-blue-500"
      />

      <div className="mt-6">
        <label
          htmlFor="cipherFile"
          className="mb-2 block font-medium"
        >
          Or Upload a .txt File
        </label>

        <input
          id="cipherFile"
          type="file"
          accept=".txt"
          className="block w-full rounded-lg border border-slate-700 bg-slate-950 p-3"
        />
      </div>

      <button
        className="mt-8 rounded-xl bg-blue-600 px-8 py-4 font-semibold hover:bg-blue-700 transition"
      >
        Predict Algorithm
      </button>
    </div>
  );
}