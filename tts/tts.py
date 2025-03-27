import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# STEP 1: Initialize TTS model
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True) # need to load model for every language 
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True) # for multi language support it only supports a voice cloning model, need to provide a voice sample for that 

speakers = tts.speakers
print(f"Available speakers: {speakers}")
speaker = speakers[1]  # Using the first available speaker

# STEP 2: Generate speech
text = "This is a test of speech synthesis with a local model."
output_file = "output.wav"
tts.tts_to_file(text=text, file_path=output_file, speaker=speaker) 
# for multi language replace speaker parameter with: 
#     speaker_wav=reference_audio,  # This is the key parameter you were missing
#    language="en"  # Also needed since it's a multilingual model

print(f"Speech generated and saved to {output_file}")

# if __name__ == "__main__":
#     # Generate speech

