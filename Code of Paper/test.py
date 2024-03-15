import numpy as np
import librosa
import matplotlib.pyplot as plt

# 画出梅尔谱图
def draw_mel_pic(sound_path):
    wavform, sr = librosa.load(sound_path)
    specgram = librosa.feature.melspectrogram(y=wavform, sr=sr)
    print(np.shape(specgram))

    mel_spect = librosa.power_to_db(specgram, ref=np.max)
    librosa.display.specshow(mel_spect, y_axis='mel', fmax=sr / 2, x_axis='time')
    plt.title('Mel Spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.show()

if __name__ == '__main__':
    sound_path='D:\dataset\CN-Celeb_flac\eval\enroll/id00814-enroll.flac'.replace('\\','/')
    draw_mel_pic(sound_path)

