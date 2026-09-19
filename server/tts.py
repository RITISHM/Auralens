from kokoro import KPipeline
import soundfile as sf
import numpy as np
import librosa

pipeline = KPipeline(lang_code='h', device='cuda')
print("TTS done")
def text_to_speech(text, response_audio_path):
   
   generator = pipeline(text, voice='af_heart')

   all_audio = []
   for i, (gs, ps, audio) in enumerate(generator):
      all_audio.append(audio)

   final_audio = np.concatenate(all_audio)

  # RESAMPLE to 16k cleanly
   resampled_audio = librosa.resample(final_audio, orig_sr=24000, target_sr=16000)

   sf.write(response_audio_path, resampled_audio, 16000)
