# 提取梅尔谱
import os
import torchaudio
import numpy as np
import librosa
import matplotlib.pyplot as plt

def get_mel_torchaudio(sound_path,feature_sound_path):
    waveform, sample_rate = torchaudio.load(sound_path)
    # 梅尔谱
    specgram = torchaudio.transforms.MelSpectrogram()(waveform)
#     存储mel文件
    np.save(feature_sound_path,specgram.numpy())

def get_mel_librosa(sound_path,feature_sound_path):
    wavform, sr = librosa.load(sound_path)
    specgram = librosa.feature.melspectrogram(y=wavform, sr=sr)
    np.save(feature_sound_path, specgram)
    print(np.shape(specgram))

    mel_spect = librosa.power_to_db(specgram, ref=np.max)
    librosa.display.specshow(mel_spect, y_axis='mel', fmax=sr / 2, x_axis='time')
    plt.title('Mel Spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.show()

def create_Feature(data_dir,detail_dir,features_file_path):
    os.chdir(detail_dir)
    os.makedirs(features_file_path)# 建立新文件夹，存放特征文件

    dirs = sorted(os.listdir(data_dir))
    for label, d in enumerate(dirs):
        lis=os.listdir(os.path.join(data_dir, d))
        os.chdir(os.path.join(detail_dir,features_file_path))
        os.makedirs(d)
        for file in lis:
            if file.split('.')[-1]=='wav':
                savedir=os.path.join(data_dir, d).replace('\\', '/')
                # 单个wav文件路径
                sound_path = os.path.join(data_dir, d, file).replace('\\', '/')
                # 单个特征文件的路径
                # D:/dataset/CN-test-feature/id00000/singing-01-001.npy
                # detaile_dir='D:/dataset/'  features_file_path='/CN-test-feature' d='/id00000'
                feature_sound_path=os.path.join(detail_dir,features_file_path,d,file).replace('.wav','.npy').replace('\\','/')
                # 特征提取  两种方式
                # get_mel(sound_path, feature_sound_path)
                get_mel_librosa(sound_path, feature_sound_path)


if __name__ == '__main__':
    features_file_path = 'CN-test-feature' #相对路径前面不用‘/’
    detail_dir = 'D:/dataset'  # 目标文件夹上一级文件夹
    data_dir='D:/dataset/CN_test'
    create_Feature(data_dir,detail_dir,features_file_path)
    # C:\Users\tkdg\Desktop\test
    # create_cn_celeb(data_dir='C:/Users/tkdg/Desktop/test/')