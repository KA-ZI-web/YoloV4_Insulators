'''
生成图片的文件名的列表，为了后面annotation做准备，后续还需要运行voc_annotation
'''
import os
import random 
 
xmlfilepath=r'./VOCdevkit/VOC2007/Annotations/labels'#标注文件（xml文件）地址
saveBasePath=r"./VOCdevkit/VOC2007/ImageSets/Main/"#输出文件地址

#数据集较小所以全部用来当做测试集，这样生成的文件中val.txt（验证集）和test.txt（测试集）文件为空
trainval_percent=1#100%训练
train_percent=1#100%训练

'''获取所有XML标注文件'''
temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)#将标注文件保存到列表

'''划分数据集'''
num=len(total_xml)  
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)  
trainval= random.sample(list,tv) #trainval：训练+验证集的索引
train=random.sample(trainval,tr) #train：训练集的索引
print("train and val size",tv)#trainval集大小
print("traub suze",tr)#train集大小

'''生成文件列表'''
ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')#训练＋验证集
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')#测试集，为空
ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')#训练集
fval = open(os.path.join(saveBasePath,'val.txt'), 'w')#验证集，为空
 
for i  in list:  
    name=total_xml[i][:-4]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
