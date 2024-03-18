# 画出梅尔谱图

import numpy as np
import librosa
import matplotlib.pyplot as plt

def draw_mel_pic(sound_path):
    wavform, sr = librosa.load(sound_path)
    print(np.shape(wavform))
    # print(wavform)

    wavform,_=librosa.effects.trim(wavform,top_db=20)#静音消除
    specgram = librosa.feature.melspectrogram(y=wavform, sr=sr)
    print(np.shape(specgram))
    # print(specgram)

    mel_spect = librosa.power_to_db(specgram, ref=np.max)
    librosa.display.specshow(mel_spect, y_axis='mel', fmax=sr / 2, x_axis='time')
    plt.title('Mel Spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.show()

if __name__ == '__main__':
    sound_path='D:\dataset\CN-Celeb_flac\eval\enroll/id00814-enroll.flac'.replace('\\','/')
    draw_mel_pic(sound_path)

