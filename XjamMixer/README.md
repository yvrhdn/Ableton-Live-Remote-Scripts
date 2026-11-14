# XjamMixer

Remote Script for the **[ESI Xjam](https://www.esi-audio.com/products/xjam/)** (6 endless encoders + 16 pressure-sensitive pads).

## What it does

- Encoder 1 (top left): cycle the selected track — regular tracks, then return tracks, then master
- Top middle / top right: pan / volume of the selected track
- Bottom row: Send A/B/C of the selected track
- Pads are intentionally not scripted — with Track enabled on the Xjam's input port they play natively on armed tracks

## Hardware setup

Use the free [Xjam Editor](https://www.esi-audio.com/support/download/). Factory defaults already work if you only switch the encoders to **Relative 2s Complement**: channel 1, **CCs 3, 9, 12, 13, 14, 15** (verified via MIDI monitor), values 1/127. Pads stay in note mode, notes 36–51. The constants at the top of `XjamMixer.py` must match the hardware scene.

## Install

See the [top-level README](../README.md#install). Keep Track enabled on the Xjam's input port so the pads reach Live.
