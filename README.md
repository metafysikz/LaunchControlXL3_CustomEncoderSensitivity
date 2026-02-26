# LaunchControlXL3_CustomEncoderSensitivity
This repository contains a modified MIDI Remote Script for the Novation Launch Control XL 3. It fixes the default sluggish "slow-turning" behavior of the encoders in DAW mode, allowing for fast, 1-turn sweeps from 0% to 100%—essential for live performance, dub-style mixing, and quick parameter adjustments.

Out of the box, the encoders on the Launch Control XL 3 are locked to a relatively slow, high-resolution response in DAW mode. While great for fine-tuning, this makes it difficult to "flick" a parameter from 0% to 100% in a single smooth motion—a common requirement for live performance and dub-style mixing.
This custom script injects a mapping_sensitivity multiplier directly into the Ableton Live 12 API, allowing you to fine-tune the encoder response to your exact preference without losing any of the controller 'smart' script functions (e.g., display feedback, etc.)

How it Works
This repository provides a raw elements.py file. By replacing the compiled component in a copy of the default script, you can override the hard-coded "Linear Binary Offset" math that Ableton uses to interpret the XL 3's relative encoders.

Installation Instructions
1. Locate the original script: Go to your Ableton Live 12 application folder and navigate to MIDI remote scripts:
e.g.: Windows: C:\ProgramData\Ableton\Live 12 Suite\Resources\MIDI Remote Scripts
e.g.: Mac: Show Package Contents > Contents/App-Resources/MIDI Remote Scripts
2. Create a new folder called 'Launch_Control_XL_3_CustomSensitivity' and unpack the files from this repo in that folder.
3. Open the 'elements.py' file with a notepad or any other simple editor, and look for the 'mapping_sensitivity' parameters that is present on two lines of code. Change this setting to your desired preference. The current setting (2.0) feels optimal for me.
4. Open Ableton and go to Preferences > Link/Tempo/MIDI and switch Control Surface 'Launch_Control_XL_3' to 'Launch_Control_XL_3_CustomSensitivity', leaving all the other MIDI settings of the MIDI controller as is.
5. Updating Settings: If you change the sensitivity later, close Ableton and delete the __pycache__ folder inside your script folder. This forces Ableton to recompile your changes on the next launch.
