'''
将VOC格式的XML标注转换为YOLO训练所需要的TXT格式标注文件。
'''

import xml.etree.ElementTree as ET
from os import getcwd

#生成2007年份的train,val,test集
sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

# 注意这个类名字需要和VOC数据集中标注的相同
classes = ["insulator"]

'''核心转换函数'''
def convert_annotation(year, image_id, list_file):
    in_file = open('VOCdevkit/VOC%s/Annotations/labels/%s.xml'%(year, image_id))
    # 使用ElementTree（库）解析XML文件
    tree=ET.parse(in_file)
    root = tree.getroot()

    #标注数据处理(跳过难例和不在classes定义的列表中的对象)
    for obj in root.iter('object'):
        difficult = 0 
        if obj.find('difficult')!=None:
            difficult = obj.find('difficult').text
            
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue

        #坐标转换
        cls_id = classes.index(cls)#获取ID
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

'''主处理流程'''
for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    #创建新的标注文件2007_train.txt
    list_file = open('VOCdevkit/VOC%s/ImageSets/Main/%s_%s.txt'%(year, year, image_set), 'w')

    #写入结果
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/images/%s.jpg'%(wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()
