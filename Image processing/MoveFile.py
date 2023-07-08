#将一个文件中的图片转移到另一个文件中

# -*- coding:utf8 -*-
import os
from PIL import Image
import numpy as np



path = ''
savedpath = ''

if not os.path.exists(savedpath):
    os.makedirs(savedpath)

filelist = os.listdir(path)

for item in filelist:
    im = Image.open(path + item)  # 打开图片
    im.save(savedpath + item)
    print('item of %s is saved at %s ' % (item,savedpath))
