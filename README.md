# LaunchControlXL3_CustomEncoderSensitivity
This repository contains a modified MIDI Remote Script for the Novation Launch Control XL 3. It fixes the default sluggish "slow-turning" behavior of the encoders in DAW mode, allowing for fast, 1-turn sweeps from 0% to 100%—essential for live performance, dub-style mixing, and quick parameter adjustments.

Out of the box, the encoders on the Launch Control XL 3 are locked to a relatively slow, high-resolution response in DAW mode. While great for fine-tuning, this makes it difficult to "flick" a parameter from 0% to 100% in a single smooth motion—a common requirement for live performance and dub-style mixing.
This custom script injects a mapping_sensitivity multiplier directly into the Ableton Live 12 API, allowing you to fine-tune the encoder response to your exact preference without losing OLED feedback, smart-mapping, or RGB LED functionality.

🛠 How it Works
This repository provides a raw elements.py file. By replacing the compiled component in a copy of the default script, you can override the hard-coded "Linear Binary Offset" math that Ableton uses to interpret the XL 3's relative encoders.

🚀 Installation Instructions
To keep your installation legally clean and compatible with future updates, follow these steps:

Locate the original script: Go to your Ableton Live 12 application folder and find:

e.g.,: Windows: C:\ProgramData\Ableton\Live 12.x\Resources\MIDI Remote Scripts\Launch_Control_XL_3

e.g., Mac: Show Package Contents > Contents/App-Resources/MIDI Remote Scripts/Launch_Control_XL_3





Activate: Restart Ableton. Go to Preferences > Link/Tempo/MIDI and switch 'Launch_Control_XL_3' to 'Launch_Control_XL_3_CustomSensitivity' as your Control Surface, leaving all the other MIDI settings of the MIDI controller as is.
