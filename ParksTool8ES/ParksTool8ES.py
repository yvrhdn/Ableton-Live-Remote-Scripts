from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Generic.Devices import best_of_parameter_bank

# --- Hardware constants: match these to your 8ES web configuration ---
CHANNEL     = 0                                    # MIDI channel 1 (zero-indexed)
ENCODER_CCS = (16, 17, 18, 19, 20, 21, 22, 23)     # one CC per encoder
PUSH_NOTES = (60, 61, 62, 63, 64, 65, 66, 67)      # one note per encoder push


class ParksTool8ES(ControlSurface):

    def __init__(self, c_instance):
        super(ParksTool8ES, self).__init__(c_instance)
        with self.component_guard():
            # Encoders are endless and send relative deltas
            # (1 = +1 step CW, 127 = -1 step CCW -> two's complement).
            encoders = [
                EncoderElement(MIDI_CC_TYPE, CHANNEL, cc,
                               Live.MidiMap.MapMode.relative_two_compliment)
                for cc in ENCODER_CCS
            ]
            # Encoder push switches: momentary buttons.
            pushes = [
                ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, note)
                for note in PUSH_NOTES
            ]
            for index, button in enumerate(pushes):
                button.add_value_listener(self._make_reset_handler(index))
            # The DeviceComponent binds the encoders to the appointed
            # ("blue hand") device and follows device selection.
            device = DeviceComponent()
            device.set_parameter_controls(tuple(encoders))
            self.set_device_component(device)
        self.show_message('ParksTool 8ES: 8 encoders on selected device')

    def _make_reset_handler(self, index):
        def _reset(value):
            if not value:                          # ignore release
                return
            device = self._current_device()
            if device is None:
                return
            # Bank 0 of a DeviceComponent = the device's "best" parameters,
            # the same list best_of_parameter_bank returns.
            params = best_of_parameter_bank(device)
            if index < len(params) and params[index].is_enabled:
                params[index].value = params[index].default_value
        return _reset

    def _current_device(self):
        song = self.song()
        device = song.appointed_device
        if device is None:
            track = song.view.selected_track
            if track is not None:
                device = track.view.selected_device
        return device


def create_instance(c_instance):
    return ParksTool8ES(c_instance)
