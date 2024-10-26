import warnings
import time
warnings.filterwarnings('ignore')

from ultralytics import YOLO
if __name__ == '__main__':
    # 记录训练开始时间
    start_time = time.time()
    model = YOLO(r'./ultralytics/cfg/models/11/yolo11_ACConv2d.yaml')
    # model = YOLO('yolo11n.pt')
    # model.train(data=r'/mnt/result2/datasets/cityscapes.yaml',
    # model.train(data=r'D:\way\yolo\Datasets\Normal_to_Foggy\voc.yaml',
    # model.train(data=r'D:\\way\\yolo\\Datasets\\cityscapes-2\\city.yaml',
    model.train(data=r'/mnt/RTTS/dataset.yaml',
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
    name='exp',
    half=True)

    # 记录训练结束时间
    end_time = time.time()

    # 计算训练时长
    training_time = end_time - start_time
    hours, rem = divmod(training_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print(f"yolov11_2训练完成！总时长: {int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒")

