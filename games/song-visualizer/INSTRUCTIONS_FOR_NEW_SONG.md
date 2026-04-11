# Instructions for Adding a New Song Visualization

This is the playbook for a future agent to follow each time the user wants a new song visualization added to the `song-visualizer` subproject. Work through every phase in order; do not skip ahead.

---

## Phase A — Conversation with the User

**Before writing a single line of code**, establish what you are building.

1. **Ask what song** the user wants visualized. Get the full title and composer.

2. **Confirm MIDI availability.** Some genres have excellent MIDI coverage; others don't:
   - Good coverage: classical repertoire (Bach, Beethoven, Chopin, …), video game OSTs, older pop and rock, jazz standards
   - Poor coverage: recent pop/hip-hop, music with complex production that doesn't translate to MIDI

3. **Discuss the aesthetic direction together.** Ask:
   - What mood or feeling should the visualization evoke?
   - Are they thinking abstract/generative, or more literal/illustrative?
   - Any color palettes, references, or visual styles they have in mind?
   - Should it feel calm and minimal, or dense and energetic?
   - Are there specific moments in the song they want the visuals to react to?

   The goal is a visualization that feels handmade and specific to this song — not a generic template output. You cannot get there without a creative brief.

4. **Do not start coding until there is a clear creative direction.** A bullet-point summary of the agreed aesthetic is sufficient before moving to Phase B.

---

## Phase B — Acquiring the MIDI

1. **Choose a slug** for the song folder: lowercase, hyphen-separated, no spaces (e.g. `fur-elise`, `moonlight-sonata`, `tetris-theme`).

2. **Search for a MIDI file.** Reasonable starting points:
   - [bitmidi.com](https://bitmidi.com)
   - [Mutopia Project](https://www.mutopiaproject.org) (classical, public domain)
   - [VGMusic](https://www.vgmusic.com) (video game music)
   - Search `site:github.com midi <song name>` for community MIDI repos

3. **Download the MIDI** to `games/song-visualizer/songs/<slug>/song.mid`.

4. **Inspect the MIDI structure before building anything.** Write a quick in-browser test page or Node script that parses the file with `@tonejs/midi` and logs:
   - Number of tracks and their names
   - Total duration
   - Tempo and time signature
   - Note count per track
   - Pitch range (lowest and highest MIDI note)
   - A sample of the first 20 notes (time, pitch, velocity, duration)

   This tells you what musical material you actually have. A MIDI file that looks right by filename can have the wrong tempo, be cut short, or be missing expected tracks.

5. **If the MIDI is clearly wrong** (tempo wildly off, tracks missing, very short), try a different source before proceeding.

---

## Phase C — Authoring the Visualization

1. **Create the song folder:**
   ```
   games/song-visualizer/songs/<slug>/
   ```

2. **Copy the template files:**
   ```bash
   cp games/song-visualizer/template/template.html  games/song-visualizer/songs/<slug>/index.html
   cp games/song-visualizer/template/template.README.md  games/song-visualizer/songs/<slug>/README.md
   ```

3. **Update `MIDI_PATH`** in `index.html` to `'./song.mid'` (it should already be that, but confirm).

4. **Replace the placeholder `drawFrame` function** with a real visualization authored for this song. Use the MIDI data you inspected in Phase B:

   | MIDI data | Visual idea |
   |-----------|-------------|
   | Pitch (note number) | Vertical position, hue on a color scale |
   | Velocity | Brightness, size, opacity |
   | Note duration | Particle lifetime, streak length |
   | Track identity | Distinct visual layer or shape type |
   | Note density / polyphony | Intensity, speed, zoom level |
   | Tempo changes | Animation pace |
   | Section boundaries | New background color, new visual motif |

5. **Consider the synth voice.** The template uses `PolySynth(Synth)` with a triangle oscillator. Match the voice to the piece:
   - Soft/gentle: sine oscillator, long release
   - Plucked strings: fast attack, short decay, low sustain
   - Harsh/electronic: `FMSynth` or `AMSynth`
   - Percussive: `MetalSynth` or `MembraneSynth` for individual tracks

6. **Consider pre-computing a timeline.** Rather than reacting only to `activeNotes` at render time, you can parse the MIDI upfront, build a sorted array of timestamped events (note-on, note-off, section changes), and look them up during the render loop. This enables "anticipation" effects and cleaner section transitions.

7. **The visualization should feel bespoke.** At minimum, the color palette and motion style should be intentional choices for this specific piece, not defaults left over from the template.

---

## Phase D — Testing

1. **Serve via the HTTP server:**
   ```
   http://localhost:8080/games/song-visualizer/songs/<slug>/index.html
   ```

2. **Use Playwright MCP to:**
   - Navigate to the URL
   - Click the Play button
   - Take screenshots at multiple timestamps (early in the piece, middle, a climax moment, near the end)
   - Check `browser_console_messages` — there should be **zero JavaScript errors**

3. **Iterate.** Do not consider the song done after one pass. Plan for at least two or three rounds of:
   - Screenshot → identify what looks wrong or bland → adjust `drawFrame` → screenshot again

4. **Save a representative screenshot:**
   ```
   games/song-visualizer/songs/<slug>/screenshot.png
   ```
   Choose a moment that shows the visualization at its best — ideally a dense or climactic section.

5. **Verify audio transport state** via `browser_evaluate`:
   ```js
   () => ({
     transportState: Tone.Transport.state,
     audioContextState: Tone.context.state
   })
   ```
   After clicking Play, `transportState` should be `"started"` and `audioContextState` should be `"running"`.

---

## Phase E — Delivery

1. **Fill in `songs/<slug>/README.md`** — replace all `{PLACEHOLDER}` values with real content.

2. **Append the new song to `games/song-visualizer/README.md`** under the `## Songs` section:
   ```markdown
   - [Song Title — Composer](songs/<slug>/)
   ```

3. **Commit and push** to the working branch with a message like:
   ```
   Add <song title> visualization

   - MIDI: <source>
   - Aesthetic: <one sentence summary>
   ```

4. **Deliver the preview link** to the user:
   ```
   https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{BRANCH}/games/song-visualizer/songs/<slug>/index.html
   ```

---

## Checklist Before Declaring Done

- [ ] MIDI file is present at `songs/<slug>/song.mid`
- [ ] `index.html` loads libraries from `../../lib/Tone.js` and `../../lib/Midi.js` (no CDN URLs)
- [ ] No JavaScript errors in browser console
- [ ] Play button works and audio context reaches `"running"` state
- [ ] `drawFrame` is a real, bespoke visualization — not the template stub
- [ ] Screenshot saved at `songs/<slug>/screenshot.png`
- [ ] `songs/<slug>/README.md` fully filled in
- [ ] New song appended to `games/song-visualizer/README.md`
- [ ] Committed and pushed

---

## Things to Avoid

- Do not skip Phase A. The aesthetic discussion is not optional bureaucracy — it is what makes the visualization worth building.
- Do not reference libraries from a CDN at runtime. Always use `../../lib/Tone.js` and `../../lib/Midi.js`.
- Do not try to work with MP3 files. This architecture is MIDI-only by design.
- Do not leave the template `drawFrame` stub in the final visualization. Replace it entirely.
- Do not commit without running at least one screenshot verification pass.
