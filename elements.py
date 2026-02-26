# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: '..\\..\\..\\output\\Live\\win_64_static\\Release\\python-bundle\\MIDI Remote Scripts\\Launch_Control_XL_3\\elements.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2025-08-26 07:19:57 UTC (1756192797)

from ableton.v3.base import nop
from ableton.v3.control_surface import ElementsBase, MapMode
from Launchkey_MK4.display_target import DisplayTargetElement
from . import midi
from .colored_encoder import ColoredEncoderElement
class Elements(ElementsBase):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.add_modifier_button(63, 'Shift_Button', channel=6)
        self.add_button(30, 'Encoder_Mode_Element', channel=6)
        self.add_button(31, 'Encoder_User_Mode_Element', channel=6)
        self.add_button(65, 'Daw_Control_Mode_Button')
        self.add_button(66, 'Daw_Mixer_Mode_Button')
        self.add_button(102, 'Track_Right_Button')
        self.add_button(103, 'Track_Left_Button')
        self.add_button(104, 'Novation_Button')
        self.add_button(106, 'Page_Up_Button')
        self.add_button(107, 'Page_Down_Button')
        self.add_button(116, 'Play_Button')
        self.add_button(118, 'Record_Button')
        self.add_button_matrix([range(37, 45)], 'Daw_Control_Buttons')
        self.add_button_matrix([range(45, 53)], 'Daw_Mixer_Buttons')
        self.add_modified_control(control=self.play_button, modifier=self.shift_button)
        self.add_modified_control(control=self.track_right_button, modifier=self.shift_button)
        self.add_modified_control(control=self.track_left_button, modifier=self.shift_button)
        self.add_modified_control(control=self.page_up_button, modifier=self.shift_button)
        self.add_modified_control(control=self.page_down_button, modifier=self.shift_button)
        self.add_encoder_matrix([range(5, 13)], 'Faders', channels=15)
        self.add_button_matrix([range(5, 13)], 'Fader_Touch_Elements', channels=14, is_private=True)
        # ==========================================
        # ENCODER SENSITIVITY FIX
        # Change "mapping_sensitivity" in the two lines below to adjust the speed / acceleration / sensitivity.
        # 1.0 is default/slow, 3.0 is fast, 5.0 is extreme. I believe 2 is a good setting.
        # ==========================================
        self.add_matrix([range(77, 85), range(85, 93)], 'Upper_Encoders', map_mode=MapMode.LinearBinaryOffset,channels=15, element_factory=ColoredEncoderElement, mapping_sensitivity=2.0)
        self.add_matrix([range(93, 101)], 'Lower_Encoders', map_mode=MapMode.LinearBinaryOffset, channels=15,element_factory=ColoredEncoderElement, mapping_sensitivity=2.0)
        #
        self.add_button_matrix([range(77, 101)], 'Encoder_Touch_Elements', channels=14, is_private=True)
        self.add_sysex_element(midi.make_connection_message()[:(-2)], 'Connection_Element')
        self.add_display_command_for_target('Static', 53, 9)
        self.add_display_command_for_target('Temp', 54, 3, disable_caching=True)
        for i in range(8):
            self.add_display_command_for_target('Fader_{}'.format(i), 5 + i, 3)
        for i in range(16):
            self.add_display_command_for_target('Upper_Encoder_{}'.format(i), 13 + i, 3)
        for i in range(8):
            self.add_display_command_for_target('Lower_Encoder_{}'.format(i), 29 + i, 3)
        self.encoder_mode_element.send_value = nop
    def add_display_command_for_target(self, name, target, num_fields, disable_caching=False):
        self.add_element('{}_Display_Command'.format(name), DisplayTargetElement, midi.SYSEX_HEADER, target, num_fields, disable_caching=disable_caching)