
import pretty_midi
import numpy as np
import soundfile as sf

def midi_to_wav(midi_file, wav_file):
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    audio_data = midi_data.fluidsynth()
    audio_data = audio_data / np.max(np.abs(audio_data))  
    sf.write(wav_file, audio_data, 44100, subtype='PCM_16')
