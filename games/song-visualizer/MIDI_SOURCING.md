# MIDI Sourcing Guide

How to find, download, and validate MIDI files for the song-visualizer subproject.
Written after live experimentation in the sandboxed Claude Code environment (April 2026).

---

## The Core Problem

Getting a good MIDI file has three distinct challenges:

1. **Reachability** — most MIDI sites are blocked from this VM environment. Only `raw.githubusercontent.com` (and `github.com`) are reliably reachable during agent sessions.
2. **Quality** — a file can have the right filename but wrong tempo, missing tracks, or only one instrument.
3. **Multi-instrument** — the majority of freely available MIDIs are solo piano. If you want orchestral/band sound, you need to specifically seek multi-track files.

---

## What Works Right Now (No Manual Steps Needed)

### The Tonejs/Midi Test Repository

**URL pattern:** `https://raw.githubusercontent.com/Tonejs/Midi/master/test/midi/<path>`

This is the single most reliable source the agent can use autonomously. These are the test fixtures for the `@tonejs/midi` library — the same library vendored as `lib/Midi.js` here. They parse cleanly, have correct tempos, and cover a useful range of composers and complexity.

#### Full catalog

| File (relative path) | Fmt | Instr. tracks | Notes | Duration | What it is |
|---|---|---|---|---|---|
| `bach/bach_format0.mid` | 0 | 1 | 415 | 70 s | Bach — single-track (what the current bach-format0 song uses) |
| `bach/bach_846.mid` | 1 | 6 | 1,284 | 140 s | Bach — WTC Book I No.1 in C major (Prelude + 4-voice Fugue) |
| `bach/bach_847.mid` | 1 | 5 | 1,845 | 138 s | Bach — WTC Book I No.2 in C minor |
| `bach/bach_850.mid` | 1 | 6 | 1,503 | 124 s | Bach — WTC Book I No.5 |
| `bartok/concerto_for_orchestra_1.mid` | 1 | **35** | 19,083 | 447 s | **Bartók — Concerto for Orchestra, Mvt 1** — full orchestra |
| `beethoven/symphony_7_2.mid` | 1 | **12** | 6,077 | 277 s | **Beethoven — Symphony No. 7, 2nd mvt** — winds + full strings |
| `beethoven/symphony_7_2_singletrack.mid` | 1 | 1 | ~6k | ~277 s | Same piece, collapsed to one track |
| `debussy/childrens_corner_1.mid` | 1 | 2 | 1,110 | 151 s | Debussy — Doctor Gradus ad Parnassum |
| `debussy/claire_de_lune.mid` | 1 | 2 | 1,491 | 162 s | Debussy — Clair de lune |
| `debussy/menuet.mid` | 1 | 2 | 2,311 | 155 s | Debussy — Menuet |
| `debussy/passepied.mid` | 1 | 2 | 2,144 | ~600 s | Debussy — Passepied (tempo encoded oddly — verify) |
| `debussy/prelude.mid` | 1 | 2 | 1,739 | 177 s | Debussy — Prelude |
| `joplin/TheEntertainer.mid` | 1 | 2 | 2,616 | 153 s | Scott Joplin — The Entertainer (ragtime, piano) |
| `tchaikovsky_seasons.mid` | 1 | 1 | 1,505 | 263 s | Tchaikovsky — The Seasons No.6 (piano) |

**Download command (agent use):**
```bash
curl -s -o games/song-visualizer/songs/<slug>/song.mid \
  "https://raw.githubusercontent.com/Tonejs/Midi/master/test/midi/<path>"
```

**Best picks for variety:**
- **Most instruments:** `bartok/concerto_for_orchestra_1.mid` — 35 instrument tracks covering Piccolo, Flute, Oboe, English Horn, Clarinets, Bassoon, Horns, Trumpets, Trombones, Tuba, Timpani, Harp, Violins, Viola, Cello, Contrabass
- **Clean orchestra (shorter):** `beethoven/symphony_7_2.mid` — 12 tracks, Flutes, Oboes, Clarinets, Bassoons, Horns, Trumpets, Timpani, Violin I/II, Viola, Cello, Bass
- **Multi-voice piano:** `bach/bach_846.mid` — 6 tracks (right hand, left hand, 4 fugue voices) — good for layered per-track visuals

---

## MIDI Format 0 vs Format 1 — Both Work

- **Format 0:** All notes collapsed into one track. Simpler, but you lose per-instrument data. The existing Bach song uses this.
- **Format 1:** Multiple tracks, each with a name and its own notes. Better for orchestral visuals. `beethoven/symphony_7_2.mid` was verified to parse and load correctly in the browser via Midi.js.

The template's `midi.tracks.forEach(...)` loop handles both formats correctly.

---

## Blocked Sources (Cannot Be Fetched by the Agent)

These sites are unreachable from the sandboxed VM environment. HTTP 000 = connection refused/timeout; HTTP 403 = server actively blocks programmatic requests.

| Site | Status | Notes |
|---|---|---|
| `bitmidi.com` | HTTP 000 | Large free collection, no account needed — **user can download manually** |
| `mfiles.co.uk` | HTTP 000 | Classical collection, no account — **user can download manually** |
| `mutopiaproject.org` | HTTP 000 | Public domain classical, no account — **user can download manually** |
| `vgmusic.com` | HTTP 000 | Video game music, no account — **user can download manually** |
| `freemidi.org` | HTTP 000 | Mixed genres, no account — **user can download manually** |
| `midiworld.com` | HTTP 000 | Classical + pop, no account — **user can download manually** |
| `kunstderfuge.com` | HTTP 000 | 19,000+ classical files — **user can download manually** |
| `classicalarchives.com` | HTTP 000 | Large classical archive — **user can download manually** |
| `piano-midi.de` | HTTP 403 | Excellent high-quality piano MIDIs — **user can download manually** |
| `musescore.com` | HTTP 000 | Huge community library; requires account for MIDI export |
| `archive.org` | HTTP 000 | Internet Archive MIDI collections |

---

## How to Get a File the Agent Can't Download (User Workflow)

When none of the Tonejs test files fit the desired song:

1. **User visits one of the working sites above** (bitmidi.com and mfiles.co.uk are the easiest — no account, direct download links).
2. **User downloads the `.mid` file** to their machine.
3. **User commits it to the repo** at `games/song-visualizer/songs/<slug>/song.mid`.
4. **Agent pulls the latest branch** and continues from Phase C of `INSTRUCTIONS_FOR_NEW_SONG.md`.

**Or:** User can paste the raw GitHub URL of any MIDI file from any public repo — the agent can fetch it directly as long as the host is `raw.githubusercontent.com`.

---

## Multi-Instrument Audio: Important Caveat

The template uses a **single `PolySynth`** for all tracks. This means every instrument (flute, violin, trumpet) plays through the same synth voice.

For a basic visualization this is fine — all notes still play in time. But it sounds like "everything on piano."

To get distinct timbres per instrument track:
- Create one synth per track in the `loadAndSchedule` function
- Map instrument names to Tone.js synth types:

```js
function synthForTrack(trackName) {
  const name = trackName.toLowerCase();
  if (name.includes('violin') || name.includes('viola') || name.includes('cello') || name.includes('bass'))
    return new Tone.PolySynth(Tone.Synth, { oscillator: { type: 'sawtooth' }, envelope: { attack: 0.05, release: 1.2 } });
  if (name.includes('flute') || name.includes('oboe') || name.includes('clarinet'))
    return new Tone.PolySynth(Tone.Synth, { oscillator: { type: 'sine' }, envelope: { attack: 0.08, release: 0.6 } });
  if (name.includes('trumpet') || name.includes('trombone') || name.includes('horn'))
    return new Tone.PolySynth(Tone.Synth, { oscillator: { type: 'square' }, envelope: { attack: 0.04, release: 0.4 } });
  if (name.includes('timpani') || name.includes('drum') || name.includes('cymbal'))
    return new Tone.PolySynth(Tone.MembraneSynth);
  if (name.includes('harp'))
    return new Tone.PolySynth(Tone.Synth, { oscillator: { type: 'triangle' }, envelope: { attack: 0.01, decay: 0.4, sustain: 0, release: 0.8 } });
  // Default: piano-adjacent
  return new Tone.PolySynth(Tone.Synth, { oscillator: { type: 'triangle' }, envelope: { attack: 0.02, release: 0.8 } });
}
```

Note: Many synths = more CPU load. For a 35-track Bartók file, consider grouping instrument families into 4–6 shared synths rather than one per track.

---

## Validating a MIDI File Before Building

Always inspect a new MIDI before writing visualization code. Paste this into the browser console after the page loads (or run it in a Node/Python script):

**Browser (after `Midi.js` loads):**
```js
async function inspectMidi(path) {
  const buf = await fetch(path).then(r => r.arrayBuffer());
  const midi = new Midi(buf);
  console.log('Tracks:', midi.tracks.length);
  console.log('Duration:', midi.duration.toFixed(1), 's');
  midi.tracks.forEach((t, i) => {
    if (t.notes.length > 0)
      console.log(`  Track ${i}: "${t.name}" — ${t.notes.length} notes, range ${t.notes[0]?.name}–${t.notes.at(-1)?.name}`);
  });
}
inspectMidi('./song.mid');
```

**Python (mido — available in this environment):**
```bash
pip install mido -q
python3 -c "
import mido, sys
mid = mido.MidiFile(sys.argv[1])
print(f'Format {mid.type}, {len(mid.tracks)} tracks')
for t in mid.tracks:
    n = sum(1 for m in t if m.type=='note_on' and m.velocity>0)
    if n: print(f'  {t.name}: {n} notes')
" games/song-visualizer/songs/<slug>/song.mid
```

**Red flags to look for:**
- Duration under 30 seconds (probably a clip, not the full piece)
- All notes on 1 track when you expected orchestral (single-track export)
- Tempo wildly off (e.g., 2× too fast — tempo stored differently than expected)
- Track names are empty or generic ("MIDI Channel 1") — less useful for per-track visuals

---

## Recommended Starting Points by Genre

| Genre | Best source | Notes |
|---|---|---|
| Classical orchestral | `Tonejs/Midi` test repo (Bartók, Beethoven) | Works autonomously, no account |
| Classical piano | `Tonejs/Midi` test repo (Bach, Debussy, Joplin) | Works autonomously |
| More classical piano | `piano-midi.de` (manually) | Very high quality, multi-voice |
| Video game music | `vgmusic.com` (manually) | Huge archive, no account |
| Pop/rock/jazz | `bitmidi.com` (manually) | Large catalog, variable quality |
| Public domain (any genre) | `mutopiaproject.org` (manually) | Verified public domain, good quality |
