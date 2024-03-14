# 将文件转换为wav
import os

def flac_to_wav(filepath, savedir):
    filename = filepath.replace('.flac', '.wav')
    savefilename = filename.split('\\')
    cmd = 'ffmpeg.exe -i ' + filepath + ' ' + savefilename[-1]
    #filepath: C:\Users\tkdg\Desktop\深度学习项目\id00800-enroll.flac
    #save_dir: C:\Users\tkdg\Desktop\深度学习项目\id00800-enroll.wav
    os.system(cmd)

def create_cn_celeb(data_dir):
    dirs = sorted(os.listdir(data_dir))
    for label, d in enumerate(dirs):
        lis=os.listdir(os.path.join(data_dir, d))
        for file in lis:
            if file.split('.')[-1]=='flac':
                savedir=os.path.join(data_dir, d)
                # print(savedir)
                sound_path = os.path.join(data_dir, d, file).replace('\\', '/')
                # print(sound_path)
                flac_to_wav(sound_path, savedir)
                # print(sound_path)
                os.remove(sound_path)

if __name__ == '__main__':
    create_cn_celeb(data_dir='D:/dataset/CN-Celeb_flac/data/')
    # C:\Users\tkdg\Desktop\test
    # create_cn_celeb(data_dir='C:/Users/tkdg/Desktop/test/')
    # create_cn_celeb2(list_path='D/dataset/train_list.txt', data_path='D:/dataset')  #暂时不要



