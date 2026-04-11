# Bach — Piano Roll Visualizer

**Composer:** Johann Sebastian Bach

![Screenshot](screenshot.png)

## Preview

[Open in browser](https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/main/games/song-visualizer/songs/bach-format0/index.html)

## MIDI Source

- **Source:** [https://raw.githubusercontent.com/Tonejs/Midi/master/test/midi/bach/bach_format0.mid](https://raw.githubusercontent.com/Tonejs/Midi/master/test/midi/bach/bach_format0.mid)
- **License:** Public domain (Bach died 1750)

## Visualization Notes

A falling piano-roll visualizer zoomed to the actual pitch range used in the piece (D3–A5, three octaves). Notes fall from top to bottom as colored bars; when they reach the keyboard strip at the bottom the corresponding key lights up with a glow.

Pitch maps to hue — low notes are amber/gold, mid notes shift through green and teal, high notes reach cool blue-violet — giving a spectrum that's easy to read at a glance. Note velocity drives brightness and saturation. A trailing fade keeps ghost echoes of recent notes visible, and a thin golden progress bar tracks position through the 70-second piece.

The synth uses a sine oscillator with a short envelope for a clean, piano-adjacent sound that suits Bach's contrapuntal style.

## Files

| File | Description |
|------|-------------|
| `index.html` | Piano roll visualizer with dynamic pitch-range zoom |
| `song.mid` | MIDI source file (415 notes, 69.5 s) |
| `screenshot.png` | Representative screenshot during playback |
| `README.md` | This file |
