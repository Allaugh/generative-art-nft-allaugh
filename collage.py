#pip install natsort
#pip install opencv-python
#pip install glob
#pip install os
#pip install PIL
import cv2
import glob
# import numpy as np
from PIL import Image
from natsort import natsorted
# from matplotlib import pyplot as plt
import os

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

#画像生成時にできたフォルダに移動
with open('images_dir.txt') as f:
    s = f.read()
    dir = s
# dir = '/Users/woo/generative-art-nft-allaugh/output/edition_11111'#最新のeditionを使わない場合は手動で設定(その場合上３行は削除)
os.chdir(dir)

# タイル状に tate × yoko 枚配置　　必要に合わせて変更
tate = 15
yoko = 15


# 所定のフォルダ内にあるjpgファイルを連続で読み込んでリスト化する
files = glob.glob("./images" + "/*.png")
# カウント用
num = 0
num2 = 0
# ファイル名が数字の場合、natsortedで
# 自然順（ファイル番号の小さい順）に1枚づつ読み込まれる
for i in natsorted(files):
    if not num == 0:
        img = Image.open(i)
        img_base = get_concat_h(img_base, img)
        num += 1
        #横にpm分画像を結合したら縦に結合して次の行へ
        if num == yoko:
            num = 0
            if not num2 == 0:
                img_base_merge = get_concat_v(img_base_merge, img_base)
                num2 +=1
                if num2 == tate:
                    break
            else:
                #１行目の処理
                img_base_merge = img_base
                num2 +=1
    else:
        #各行１列目の処理
        img_base = Image.open(i)
        num += 1


os.makedirs("collage", exist_ok=True)
img_base_merge.save('./collage/collage.png')
print(img_base_merge)