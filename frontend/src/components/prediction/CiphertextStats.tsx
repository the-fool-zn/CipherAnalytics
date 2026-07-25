type CiphertextStatsProps = {
  ciphertext: string;
};

function detectCharacterSet(text: string): string {
  const hexPattern = /^[0-9a-fA-F]+$/;
  const base64Pattern = /^[A-Za-z0-9+/=]+$/;

  if (hexPattern.test(text)) return "Hexadecimal";
  if (base64Pattern.test(text)) return "Base64";
  return "Mixed / Plain Text";
}

export default function CiphertextStats({ ciphertext }: CiphertextStatsProps) {
  const length = ciphertext.length;
  const estimatedBytes = Math.ceil(length / 2);
  const characterSet = detectCharacterSet(ciphertext);
  const isValid = length > 0;

  const stats = [
    { label: "Length", value: `${length} characters` },
    { label: "Estimated Bytes", value: `${estimatedBytes}` },
    { label: "Character Set", value: characterSet },
    { label: "Input Status", value: isValid ? "Valid" : "Empty" },
  ];

  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
      <h3 className="mb-4 text-lg font-semibold text-white">
        Ciphertext Statistics
      </h3>
      <div className="grid grid-cols-2 gap-4">
        {stats.map((stat) => (
          <div key={stat.label}>
            <p className="text-sm text-slate-400">{stat.label}</p>
            <p className="text-base font-medium text-white">{stat.value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}