"""Transcreve o vídeo com o tempo exato de cada palavra (português).
Uso: python transcrever.py VIDEO.mov
Gera: transcricao.json (palavras com início/fim) e transcricao.txt (para revisar)."""
import sys, json, subprocess, os
from faster_whisper import WhisperModel

video = sys.argv[1]
base = os.path.splitext(video)[0]
wav = base + "_16k.wav"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", video, "-ac", "1", "-ar", "16000", wav], check=True)

# large-v3 é o mais preciso; se o computador for lento, troque por "medium"
model = WhisperModel("large-v3", device="auto", compute_type="int8")
segs, _ = model.transcribe(wav, language="pt", word_timestamps=True, vad_filter=True,
                           initial_prompt="Social media, IA, prompt, {{SEU_METODO}}, Instagram, estrategista.")
words, lines = [], []
for s in segs:
    lines.append(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()}")
    for w in s.words:
        words.append({"start": round(w.start, 3), "end": round(w.end, 3), "word": w.word.strip()})
json.dump(words, open("transcricao.json", "w"), ensure_ascii=False, indent=1)
open("transcricao.txt", "w").write("\n".join(lines))
print("\n".join(lines))
print(f"\n{len(words)} palavras -> transcricao.json")
