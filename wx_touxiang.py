#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-14 14:51
# 作者:   ljk
import itchat
path = 'C:/Users/naturade/Desktop/VBN/imgs'
itchat.auto_login()
# 获取好友信息列表
import os
import math
from PIL import Image
def get_imgs():
    num = 0
    friends = itchat.get_friends(update=True)
    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"])
        file_image = open(path + "/" + str(num) + ".jpg", 'wb')
        file_image.write(img)
        file_image.close()
        num += 1

get_imgs()
itchat.logout()
ls = os.listdir(path)

xx = int(math.sqrt(len(ls)))
image = Image.new('RGBA', (160*xx, 160*xx))   # 创建640*640px的大图
x = 0
y = 0

for i in ls:
    try:
        img = Image.open(path +'/'+ i)
    except IOError:
        print("Error")
    else:
        img = img.resize((160,160),Image.ANTIALIAS)
        image.paste(img, (x * 160, y * 160))    # 粘贴位置
        x += 1
        if x == 12:  # 换行
              x = 0
              y += 1

image.save(path + "/好友头像拼接图.png")
