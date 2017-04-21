# Feature extraction example
import numpy as np
import librosa
import librosa.feature
# Load the example clip
y, sr = librosa.load(librosa.util.example_audio_file())

# Set the hop length; at 22050 Hz, 512 samples ~= 23ms
hop_length = 512

# Separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)
print y_harmonic,y_percussive
# Beat track on the percussive signal
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
                                             sr=sr)

# Compute MFCC features from the raw signal
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
print mfcc
# And the first-order differences (delta features)
mfcc_delta = librosa.feature.delta(mfcc)
print mfcc_delta
# Stack and synchronize between beat events
# This time, we'll use the mean value (default) instead of median
#beat_mfcc_delta = librosa.feature.sync(np.vstack([mfcc, mfcc_delta]),beat_frames)

# Compute chroma features from the harmonic signal
chromagram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
print chromagram
# Aggregate chroma features between beat events
# We'll use the median value of each feature between beat frames
#beat_chroma = librosa.feature.sync(chromagram,beat_frames,aggregate=np.median)

# Finally, stack all beat-synchronous features together
#beat_features = np.vstack([beat_chroma, beat_mfcc_delta])
#print beat_features