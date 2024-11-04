import warnings
import time
warnings.filterwarnings('ignore')

from ultralytics import YOLO
if __name__ == '__main__':
    # 记录训练开始时间
    start_time = time.time()
    model = YOLO(r'./ultralytics/cfg/models/11/WDBB_FriendNet.yaml')
    # model = YOLO('yolo11n.pt')
    # model.train(data=r'/mnt/result2/datasets/cityscapes.yaml',
    # model.train(data=r'D:\way\yolo\Datasets\Normal_to_Foggy\voc.yaml',
    # model.train(data=r'D:\\way\\yolo\\Datasets\\cityscapes-2\\city.yaml',
    # model.train(data=r'/mnt/datasets/cityscapes.yaml',
    # model.train(data=r'D:/way/yolo/Datasets/datasets/cityscapes.yaml',
    model.train(data=r'D:/way/yolo/Datasets/RTTS2/dataset.yaml',
    cache=False,
    imgsz=640,
    epochs=100,
    single_cls=False,
    batch=8,
    close_mosaic=10,
    workers=0,   # win电脑最好设置为0，否则容易报线程错误
    device='cpu',
    optimizer='SGD',
    amp=True,
    project='runs/train',
    name='exp_RTTS2_W_P_1',
    half=True)


