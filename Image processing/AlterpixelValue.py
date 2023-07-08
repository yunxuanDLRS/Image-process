# -*- coding:utf8 -*-

#将某个文件中的图片进行像素值修改，修改后保存到另一个文件夹中
#常用于语义分割中设置【像素值--类别】

import os
from PIL import Image
import numpy as np

path = ''
savedpath = ''

filelist = os.listdir(path)

for item in filelist:
    im = Image.open(path + item)  # 打开图片
    width = im.size[0]  # 获取宽度
    height = im.size[1]  # 获取长度
    # data = np.asarray(im)
    # print(data.shape)
    # print(data)
    # #
    #
    for x in range(width):
        for y in range(height):
            value = im.getpixel((x, y))
            if (value == 255):
                im.putpixel((x, y), (1))
    #im = im.convert('RGB')
    im.save(savedpath + item)
    print('item of %s is saved ' % (item))
