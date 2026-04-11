# Song Visualizer

Hand-authored MIDI-driven music visualizations, running entirely in the browser with no server and no runtime CDN dependencies.

## What Is This?

Each entry in this subproject is a bespoke visualization crafted for a specific piece of music. There is no shared "look" — every visualization is authored by hand to fit its particular song. The goal is for the visuals to feel intentional and specific, not like a generic audio-reactive template.

## Why MIDI + Tone.js?

- **MIDI files contain structured note data** — pitch, timing, velocity, instrument — that makes it possible to choreograph visuals against specific musical events rather than just reacting to amplitude.
- **Tone.js synthesizes audio from MIDI in the browser**, which means no MP3 hosting, no licensing headaches, and perfect sync between audio and visuals (they share the same transport clock).
- **Vendoring the libraries locally** keeps everything self-contained and offline-capable once cloned, in keeping with the rest of the repo's "no runtime CDN" spirit.

## Folder Layout

```
games/song-visualizer/
├── lib/
│   ├── Tone.js           ← vendored Tone.js UMD build
│   └── Midi.js           ← vendored @tonejs/midi UMD build
├── template/
│   ├── template.html     ← starting-point HTML for a new song
│   └── template.README.md ← starting-point README for a song folder
├── songs/
│   └── <song-slug>/
│       ├── index.html    ← the visualizer
│       ├── song.mid      ← MIDI source
│       ├── screenshot.png
│       └── README.md
└── INSTRUCTIONS_FOR_NEW_SONG.md
```

Each song's HTML loads the vendored libraries via relative paths (`../../lib/Tone.js`), so there is exactly one copy of each library in the repo regardless of how many songs are added.

## Adding a New Song

See [INSTRUCTIONS_FOR_NEW_SONG.md](./INSTRUCTIONS_FOR_NEW_SONG.md) for the full step-by-step playbook.

## Songs

<!-- Append new entries here as songs are added, e.g.:
- [Für Elise — Beethoven](songs/fur-elise/) -->
