

#将目录中的【图片】转移到另一个文件夹
#可方向用于提出文件中的非图片数据

# -*- coding:utf8 -*-
import os
from PIL import Image
import numpy as np
import datetime

#在员名称的基础上改名
def rename(img_folder,num):
    for img_name in os.listdir(img_folder):  # os.listdir()： 列出路径下所有的文件
        #os.path.join() 拼接文件路径
        if (img_name.split('.')[1] == 'png'):
            im = Image.open(img_folder + img_name)
            im.save('VOCdevkit/VOC2007/1/' + img_name)
            num+=1
    print("保存图片{}张".format(num))

def main():
    img_folder0 = r'' #图片的文件夹路径
    num=0
    n=rename(img_folder0,num)

if __name__=="__main__":
    main()
