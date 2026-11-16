#!/usr/bin/env bash
# Comprime um reel para ~9MB (limite de upload de 10MB) em duas passadas, sem perder qualidade visível.
# Uso: bash scripts/comprimir.sh saida/reels/video.mp4
set -e
IN="$1"; OUT="${IN%.mp4}-9mb.mp4"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
VB=$(python3 -c "print(int((9*8*1024*1024/$DUR - 128000)/1000))")
ffmpeg -y -i "$IN" -c:v libx264 -preset veryfast -b:v ${VB}k -pass 1 -an -f mp4 /dev/null
ffmpeg -y -i "$IN" -c:v libx264 -preset veryfast -b:v ${VB}k -pass 2 -c:a aac -b:a 128k -movflags +faststart "$OUT"
rm -f ffmpeg2pass-0.log ffmpeg2pass-0.log.mbtree
echo "$OUT"
