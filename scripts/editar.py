"""Editor de reels do {{SEU_ARROBA}} (padrão da equipe).
Uso: python editar.py config.json
Precisa de: transcricao.json (gerado pelo transcrever.py), ffmpeg, opencv-python, fonte Inter instalada.

Direção (anti "cara de vídeo de IA"):
- legenda sincronizada com a fala real, em frases curtas, sem pop e sem colorir palavra por palavra;
- destaque em limão só nas palavras escolhidas no config (cerca de 1 a cada 10);
- cortes secos nas pausas e dois enquadramentos alternados, como duas câmeras; zoom só em até 3 palavras;
- texto nunca sobre o rosto: o rosto é rastreado quadro a quadro e o texto vai para a área livre;
- tipografia do feed aprovado: Inter fina + Inter negrito, marca-texto limão, rótulos editoriais.
"""
import json, os, subprocess, sys, shutil
import numpy as np, cv2

cfg = json.load(open(sys.argv[1]))
SRC = cfg["video"]; OUT = cfg.get("saida", "reel-final.mp4")
W, H = 1080, 1920
TMP = "_tmp_edicao"; os.makedirs(TMP, exist_ok=True)
BLUE, LIME, WHITE = "&H00CB3101&", "&H0001FCB9&", "&H00FFFFFF&"
TOP_MIN, BOTTOM_MAX = 140, 1600          # abaixo de 1600 a interface do Instagram cobre o vídeo

# ---------- 1) palavras reais e trechos de fala ----------
words = json.load(open("transcricao.json"))
for w in words: w["word"] = w["word"].strip()
PIECES, cur = [], [words[0]]
for a, b in zip(words, words[1:]):
    if b["start"] - a["end"] > 0.35: PIECES.append(cur); cur = []
    cur.append(b)
PIECES.append(cur)
PIECES = [(max(0, p[0]["start"] - 0.06), p[-1]["end"] + 0.12) for p in PIECES]
offs, acc = [], 0.0
for s, e in PIECES: offs.append(acc); acc += e - s
TOTAL = acc
def T(t):
    for (s, e), o in zip(PIECES, offs):
        if t < s: return o
        if t <= e: return o + t - s
    return TOTAL
WM = [(T(w["start"]), T(w["end"]), w["word"]) for w in words]
def norm(x): return x.lower().strip(",.:;!?\"'“”")
def when(word, n=1):
    c = 0
    for a, b, w in WM:
        if norm(w) == norm(word):
            c += 1
            if c == n: return a, b
    raise SystemExit(f"Palavra '{word}' não encontrada na transcrição. Ajuste o config.")

# ---------- 2) vídeo: cortes secos + dois enquadramentos + zoom pontual ----------
punch = [when(p)[0] for p in cfg.get("zoom_nas_palavras", [])[:3]]
lst = []
for i, (s, e) in enumerate(PIECES):
    dur, o = e - s, offs[i]
    z0 = 1.0 if i % 2 == 0 else 1.09                     # "câmera A" e "câmera B"
    bumps = "+".join(f"0.06*exp(-pow((t-{p-o:.3f})/0.12,2))" for p in punch if o <= p <= o + dur) or "0"
    Z = f"({z0}+{bumps})"
    vf = (f"scale=w='trunc(1080*{Z}/2)*2':h='trunc(1920*{Z}/2)*2':eval=frame:flags=bicubic,"
          f"crop=1080:1920:'(iw-1080)/2':'(ih-1920)*0.35',setsar=1,fps=30,format=yuv420p")
    p = f"{TMP}/p{i:03d}.mov"; lst.append(f"file '{os.path.abspath(p)}'")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{s}", "-to", f"{e}", "-i", SRC, "-vf", vf,
        "-af", f"afade=t=in:d=0.015,afade=t=out:st={dur-0.02:.3f}:d=0.02,aresample=48000",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2", p], check=True)
open(f"{TMP}/lista.txt", "w").write("\n".join(lst))
JOINED = f"{TMP}/junto.mov"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{TMP}/lista.txt", "-c", "copy", JOINED], check=True)

# B-roll (gravações de tela, prints): entram por cima, a voz continua
for k, br in enumerate(cfg.get("broll", [])):
    a, _ = when(br["palavra"]); d = br.get("duracao", 2.0)
    tmp = f"{TMP}/broll{k}.mov"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", JOINED, "-i", br["arquivo"], "-filter_complex",
        f"[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setpts=PTS-STARTPTS+{a}/TB[b];"
        f"[0:v][b]overlay=enable='between(t,{a},{a+d})':eof_action=pass[v]", "-map", "[v]", "-map", "0:a",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-c:a", "copy", tmp], check=True)
    shutil.move(tmp, JOINED)

# ---------- 3) rastreamento do rosto ----------
cap = cv2.VideoCapture(JOINED)
cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
rows, f = [], 0
while True:
    ok, img = cap.read()
    if not ok: break
    if f % 3 == 0:
        g = cv2.cvtColor(cv2.resize(img, (540, 960)), cv2.COLOR_BGR2GRAY)
        fs = cas.detectMultiScale(g, 1.1, 5, minSize=(130, 130))
        if len(fs):
            x, y, w, h = max(fs, key=lambda r: r[2] * r[3])
            rows.append((f / 30, y * 2 - 0.12 * h * 2, (y + h) * 2 + 0.04 * h * 2))
    f += 1
FA = np.array(rows) if rows else np.zeros((0, 3))
def face(a, b):
    m = (FA[:, 0] >= a - 0.25) & (FA[:, 0] <= b + 0.25) if len(FA) else []
    return (float(FA[m, 1].min()), float(FA[m, 2].max())) if len(FA) and m.any() else (420.0, 1380.0)

# ---------- 4) textos (ASS) ----------
def ts(t):
    t = max(0, t); return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
ass = [f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter SemiBold,58,{WHITE},{WHITE},&H00000000&,&H78000000&,0,0,0,0,100,100,0,0,1,0,3,5,0,0,0,1
Style: Meta,Inter,24,{WHITE},{WHITE},&H00000000&,&H78000000&,0,0,0,0,100,100,0,0,1,0,2,5,0,0,0,1
Style: Fina,Inter Light,64,{WHITE},{WHITE},&H00000000&,&H78000000&,0,0,0,0,100,100,-1,0,1,0,3,5,0,0,0,1
Style: Forte,Inter ExtraBold,78,{WHITE},{WHITE},&H00000000&,&H78000000&,0,0,0,0,100,100,-2,0,1,0,3,5,0,0,0,1
Style: Marca,Inter ExtraBold,78,{BLUE},{BLUE},{LIME},&H00000000&,0,0,0,0,100,100,-2,0,3,14,0,5,0,0,0,1
Style: Num,Inter ExtraBold,150,{LIME},{LIME},&H00000000&,&H78000000&,0,0,0,0,100,100,-6,0,1,0,4,6,0,0,0,1
Style: Lado,Inter Medium,50,{WHITE},{WHITE},&H00000000&,&H78000000&,0,0,0,0,100,100,0,0,1,0,3,4,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"""]
BOX = []
def ev(a, b, st, txt, layer=1, y=None, h=0):
    ass.append(f"Dialogue: {layer},{ts(a)},{ts(b)},{st},,0,0,0,,{txt}")
    if y is not None: BOX.append((a, b, y - h / 2, y + h / 2, st))
def spot(a, b, h, prefer="top"):
    top, chin = face(a, b)
    up = (TOP_MIN + (top - 40 - TOP_MIN) / 2) if top - 40 - TOP_MIN >= h else None
    dn = max(chin + 25 + h / 2, 1380); dn = dn if dn + h / 2 <= BOTTOM_MAX else None
    order = [up, dn] if prefer == "top" else [dn, up]
    return next((y for y in order if y is not None), None)

def spot_fit(a, b, h, prefer="top"):
    """tenta caber em tamanho cheio; se não couber, reduz até 55%; devolve (y, escala)"""
    for sc in (1.0, 0.85, 0.7, 0.55):
        y = spot(a, b, h * sc, prefer)
        if y is not None: return y, sc
    return None, 0.55

a0, b0 = 0, TOTAL
l, r = cfg.get("rotulos_topo", ["", ""])
ev(0, TOTAL, "Meta", r"{\an4\pos(70,80)}" + l, 0); ev(0, TOTAL, "Meta", r"{\an6\pos(1010,80)}" + r, 0)

# janelas em que um destaque substitui a legenda
busy = []
g = cfg.get("gancho")
if g: busy.append((0, g.get("ate_segundos", 3.2)))
moms = []
for m in cfg.get("momentos", []):
    a, _ = when(m["palavra"]); a -= m.get("comeca_antes", 0.05); b = a + m.get("duracao", 2.5)
    moms.append((a, b, m)); busy.append((a, b))

# legenda: frases curtas da fala real
HL = {norm(x) for x in cfg.get("destacar_palavras", [])}
chunks, cur = [], []
for item in WM:
    cur.append(item); txt = " ".join(x[2] for x in cur)
    if item[2][-1] in ".?!:" or len(txt) > 22 or len(cur) == 4: chunks.append(cur); cur = []
if cur: chunks.append(cur)
for i, ch in enumerate(chunks):
    a = ch[0][0]; b = min(chunks[i + 1][0][0] if i + 1 < len(chunks) else ch[-1][1] + 0.4, ch[-1][1] + 0.5)
    if any(x - 0.05 <= a < y for x, y in busy): continue
    for x, y in busy:
        if a < x < b: b = x - 0.04
    y = spot(a, b, 76, prefer="bottom")
    if y is None: continue
    txt = " ".join((r"{\c" + LIME + "}" + w + r"{\c" + WHITE + "}") if norm(w) in HL else w for _, _, w in ch)
    ev(a, b, "Cap", r"{\an5\pos(540," + str(int(y)) + r")\fad(70,50)}" + txt, 2, y, 76)

# gancho no estilo do feed aprovado: linha fina + linha forte com marca-texto
if g:
    b = g.get("ate_segundos", 3.2); y, _ = spot_fit(0, b, 190); y = y or 300
    ev(0, b, "Fina", r"{\an5\pos(540," + str(int(y - 50)) + r")\fad(0,180)}" + g["linha_fina"], 3, y - 50, 70)
    ev(0.2, b, "Marca", r"{\an5\pos(540," + str(int(y + 45)) + r")\fad(120,180)}" + g["linha_forte"], 3, y + 45, 100)

for a, b, m in moms:
    if m["tipo"] == "dado":
        y, sc = spot_fit(a, b, 160, prefer="bottom")
        if y is None: continue
        z = r"\fscx" + str(int(100 * sc)) + r"\fscy" + str(int(100 * sc))
        ev(a, b, "Num", r"{\an6\pos(500," + str(int(y)) + r")\fad(100,160)" + z + "}" + m["numero"], 3, y, 150 * sc)
        ev(a + 0.25, b, "Lado", r"{\an4\pos(530," + str(int(y)) + r")\fad(140,160)" + z + "}" + m["texto"].replace("\n", r"\N"), 3, y, 120 * sc)
    elif m["tipo"] == "frase":
        y, sc = spot_fit(a, b, 190)
        if y is None: continue
        z = r"\fscx" + str(int(100 * sc)) + r"\fscy" + str(int(100 * sc))
        ev(a, b, "Fina", r"{\an5\pos(540," + str(int(y - 50 * sc)) + r")\fad(100,180)" + z + "}" + m["linha_fina"], 3, y - 50 * sc, 70 * sc)
        ev(a + 0.3, b, "Marca", r"{\an5\pos(540," + str(int(y + 45 * sc)) + r")\fad(100,180)" + z + "}" + m["linha_forte"], 3, y + 45 * sc, 100 * sc)

c = cfg.get("cta")
if c:
    a, _ = when(c["palavra"]); y, _ = spot_fit(a, TOTAL, 100); y = y or 300
    ev(a, TOTAL, "Marca", r"{\an5\pos(540," + str(int(y)) + r")\fad(160,0)}" + c["texto"], 3, y, 100)

open(f"{TMP}/textos.ass", "w").write("\n".join(ass) + "\n")

# ---------- 5) checagem automática (Revisor) ----------
rosto = sum(1 for a, b, y0, y1, _ in BOX if len(FA) and any(y1 > ft and y0 < fb for t, ft, fb in FA[(FA[:, 0] >= a) & (FA[:, 0] <= b)]))
fora = sum(1 for x in BOX if x[3] > BOTTOM_MAX or x[2] < TOP_MIN - 80)
print(f"Revisor: textos sobre o rosto = {rosto} | fora da área segura = {fora}")
for a, b, y0, y1, st in BOX:
    if len(FA) and any(y1 > ft and y0 < fb for t, ft, fb in FA[(FA[:, 0] >= a) & (FA[:, 0] <= b)]): print("  sobre o rosto:", st, round(a, 1), int(y0), int(y1))

# ---------- 6) áudio e exportação ----------
fonts = cfg.get("pasta_fontes", "")
sub = f"subtitles={TMP}/textos.ass" + (f":fontsdir={fonts}" if fonts else "")
graph = (f"[0:v]{sub},format=yuv420p[v];"
         "[0:a]highpass=f=80,afftdn=nf=-28,acompressor=threshold=-20dB:ratio=3:attack=5:release=90:makeup=2,"
         "equalizer=f=3500:t=q:w=1:g=2,loudnorm=I=-14:TP=-1.5:LRA=7[a]")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", JOINED, "-filter_complex", graph, "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-preset", "slow", "-b:v", "14M", "-maxrate", "16M", "-bufsize", "32M", "-profile:v", "high",
    "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT], check=True)
print(f"Pronto: {OUT} ({TOTAL:.1f}s)")
