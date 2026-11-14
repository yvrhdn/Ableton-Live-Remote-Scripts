# Ableton Live Remote Scripts

Custom MIDI Remote Scripts for Ableton Live.

## Scripts

| Script | Hardware | What it does |
|---|---|---|
| [ParksTool8ES](ParksTool8ES/) | [ParksTool 8ES](https://www.parkstool.com/products/parks-custom-encoders-8-4-midi-plug-21348) (8 push encoders) | Encoders map to the selected device's best 8 parameters; push resets a parameter to default |
| [XjamMixer](XjamMixer/) | [ESI Xjam](https://www.esi-audio.com/products/xjam/) (6 encoders + 16 pads) | Encoder 1 cycles tracks; encoders 2–6 drive volume/pan/sends of the selected track. Pads play natively |

## Install

Drop the script folder into `~/Music/Ableton/User Library/Remote Scripts/`, run `make clean`, restart Live, then pick the script under Settings → Link, Tempo & MIDI → Control Surface.

See [Ableton's guide to installing third-party remote scripts](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts).

## Development

- `make clean` — remove `__pycache__` (required after any file change; Live only scans scripts at startup)
- `make log` — show the Live log filtered to errors/tracebacks/script names

## Resources

- [_Framework / LOM reference and guides](https://midiremotescripts.structure-void.com) (unofficial, by Structure Void)
- Debug log: `~/Library/Preferences/Ableton/Live <version>/Log.txt` — Python tracebacks land here if a script fails to load
