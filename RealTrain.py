import warnings
import time
warnings.filterwarnings('ignore')

from ultralytics import YOLO
if __name__ == '__main__':
    # 记录训练开始时间
    start_time = time.time()
# python 'D:/way/yolo/yolo5-6/yolov5-6.0/train.py' --weights '' --data 'D:/way/yolo/Datasets/datasets/rain.yaml' --cfg D:/way/yolo/yolo5-6/yolov5-6.0/models/yolov5s.yaml
    model = YOLO(r'ultralytics/cfg/models/11/yolo11.yaml')
    # model = YOLO('yolo11n.pt')
    # model.train(data=r'/mnt/result2/datasets/cityscapes.yaml',
    # model.train(data=r'D:\way\yolo\Datasets\Normal_to_Foggy\voc.yaml',
    # model.train(data=r'D:\\way\\yolo\\Datasets\\cityscapes-2\\city.yaml',
    # model.train(data=r'/mnt/datasets/cityscapes.yaml',
    # model.train(data=r'/mnt/datasets/rain.yaml',
    model.train(data=r'/mnt/datasets/rain.yaml',
    cache=False,
    imgsz=640,
    epochs=100,
    single_cls=False,
    batch=8,
    close_mosaic=10,
    workers=0,   # win电脑最好设置为0，否则容易报线程错误
    device='0',
    optimizer='SGD',
    amp=True,
    project='runs/train',
    name='exp_hazy_yolov11',
    half=True)


