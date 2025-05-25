import os.path
from yolo import YOLO
from PIL import Image
import numpy as np
import glob
import cv2

yolo = YOLO()

#输入输出路径
input_Path = "img/0591.jpg"
output_dir = "./results"
output_Path = os.path.join(output_dir,"01.jpg")

#读取并转换图像
image = Image.open(input_Path).convert("RGB")
#目标检测
r_image = yolo.detect_image(image)

# 关键修复：强制3通道 + 验证
img_array = np.array(r_image)
print("Array shape:", img_array.shape)
if img_array.shape[2] == 4:  # 如果意外存在Alpha
    img_array = img_array[:, :, :3]  # 显式去除
# 转换为OpenCV格式并保存
img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
cv2.imwrite(output_Path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

#验证
print("保存后模式：",Image.open(output_Path).mode)  # 应输出 "RGB"

#显示结果
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()