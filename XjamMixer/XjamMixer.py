from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.MixerComponent import MixerComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE

# --- Hardware constants: match these to your Xjam preset ---
# Xjam encoders send relative "2's complement" values:
#   clockwise = 1 (+1 step), counter-clockwise = 127 (-1 step).
CHANNEL     = 0                                # MIDI channel 1 (zero-indexed)
ENCODER_CCS = (3, 9, 12, 13, 14, 15)           # one CC per encoder (Xjam factory defaults)

# Values the Xjam sends for one step CW / CCW
CW_VALUE    = 1
CCW_VALUE   = 127


class XjamMixer(ControlSurface):

    def __init__(self, c_instance):
        super(XjamMixer, self).__init__(c_instance)
        with self.component_guard():
            encoders = [
                EncoderElement(MIDI_CC_TYPE, CHANNEL, cc,
                               Live.MidiMap.MapMode.relative_two_compliment)
                for cc in ENCODER_CCS
            ]
            # Encoder 1 (top left): cycle the selected track.
            encoders[0].add_value_listener(self._on_track_encoder)
            # Top middle / top right: pan / volume of the selected track.
            # Bottom row: send A/B/C. The MixerComponent's selected strip
            # follows track selection. Must be registered (not just
            # constructed) or the component stays disabled and the strips
            # never receive the encoders.
            mixer = MixerComponent(1)
            self._register_component(mixer)
            mixer.set_track_offset(0)
            strip = mixer.selected_strip()
            strip.set_pan_control(encoders[1])
            strip.set_volume_control(encoders[2])
            strip.set_send_controls((encoders[3], encoders[4], encoders[5]))
        self.show_message('Xjam mixer loaded')

    def _on_track_encoder(self, value):
        # Cycle through regular tracks, then return tracks, then master —
        # same ordering MixerComponent uses for its own next/prev buttons.
        song = self.song()
        tracks = (list(song.tracks) + list(song.return_tracks)
                  + [song.master_track])
        if not tracks:
            return
        current = self.song().view.selected_track
        try:
            index = tracks.index(current)
        except ValueError:
            index = 0
        if value == CW_VALUE:
            index = min(index + 1, len(tracks) - 1)
        elif value == CCW_VALUE:
            index = max(index - 1, 0)
        else:
            return                  # multiple steps come as repeated values
        self.song().view.selected_track = tracks[index]


def create_instance(c_instance):
    return XjamMixer(c_instance)
