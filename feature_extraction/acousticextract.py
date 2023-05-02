import os
import numpy as np
import pandas as pd
import librosa as librosa
from librosa import feature

output_keys, output_values = [], []

for filename in os.listdir('audios'):
        file = os.path.join('audios', filename)
        print(filename)
        y, sampling_rate = librosa.load(file,sr=None) # load the audio file with librosa and extract various features below
        rolloff = np.mean(feature.spectral_rolloff(y=y, sr=sampling_rate))
        centroid = np.mean(feature.spectral_centroid(y=y, sr=sampling_rate))
        mfcc = np.mean(feature.mfcc(y=y, sr=sampling_rate))
        spec = np.mean(feature.chroma_stft(y=y, sr=sampling_rate))
        bandwidth = np.mean(feature.spectral_bandwidth(y=y, sr=sampling_rate))
        contrast = np.mean(feature.spectral_contrast(y=y, sr=sampling_rate))     
        feature_array = np.append([], [spec, rolloff, centroid, bandwidth, contrast, mfcc])
        output_keys.append(filename)
        output_values.append(feature_array)

df = pd.DataFrame(list(zip(output_keys, output_values)), columns=['file', 'feature vector'])
print(df.head())
df.to_pickle('./acousticfeatures.pkl')