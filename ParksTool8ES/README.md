# ParksTool8ES

Remote Script for the **[ParksTool 8ES](https://www.parkstool.com/products/parks-custom-encoders-8-4-midi-plug-21348)** (8 endless push encoders).

## What it does

- Encoders auto-map to the selected device's best 8 parameters (blue hand follows device selection)
- Pushing an encoder resets that parameter to its default value

## Hardware setup

Easiest: in the web editor at [config.parkstool.com](https://config.parkstool.com) → **File → Load from File**, pick [`8ES-config.json`](8ES-config.json), then APPLY.

Or configure each control manually (channel 1 everywhere):

| Control | Content Type | A message (CCW) | B message (CW) | Push (note) |
|---|---|---|---|---|
| Encoder 1 | MIDI Custom | CC 16, value 127 | CC 16, value 1 | Note On 60 / Off 36 |
| Encoder 2 | MIDI Custom | CC 17, value 127 | CC 17, value 1 | Note On 61 / Off 37 |
| Encoder 3 | MIDI Custom | CC 18, value 127 | CC 18, value 1 | Note On 62 / Off 38 |
| Encoder 4 | MIDI Custom | CC 19, value 127 | CC 19, value 1 | Note On 63 / Off 39 |
| Encoder 5 | MIDI Custom | CC 20, value 127 | CC 20, value 1 | Note On 64 / Off 40 |
| Encoder 6 | MIDI Custom | CC 21, value 127 | CC 21, value 1 | Note On 65 / Off 41 |
| Encoder 7 | MIDI Custom | CC 22, value 127 | CC 22, value 1 | Note On 66 / Off 42 |
| Encoder 8 | MIDI Custom | CC 23, value 127 | CC 23, value 1 | Note On 67 / Off 43 |

The A/B values are the **Relative 2's Complement** mode (127 = one step CCW, 1 = one step CW); the push note-off goes to a different note so releases don't retrigger. Set **Max Banks** to 1 in Global Variables. The constants at the top of `ParksTool8ES.py` must match this.

## Install

See the [top-level README](../README.md#install).
