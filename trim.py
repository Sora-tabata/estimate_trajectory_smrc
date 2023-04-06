

# -*- coding: utf-8 -*-
import sys
from PIL import Image
import os
from find_hood import Findhood
import numpy as np

class TrimImages():
  def __init__(self):

    #トリミング前の画像の格納先
    self.ORIGINAL_FILE_DIR = "images/"
    #トリミング後の画像の格納先
    self.TRIMMED_FILE_DIR = "image_0/"
    self.width = Image.open(self.ORIGINAL_FILE_DIR+os.listdir(self.ORIGINAL_FILE_DIR)[0]).width
    print(self.width)

#画像パスと、左上座標、右下座標を指定して、トリミングされたimageオブジェクトを返す。
  def trim(self, path, left, top, right, bottom):
    im = Image.open(path)
    im_trimmed = im.crop((left,top,right,bottom))
    return im_trimmed

  def createTrimedImages(self):
    if os.path.isdir(self.TRIMMED_FILE_DIR) == False:
      os.makedirs(self.TRIMMED_FILE_DIR)

    #トリミングする左上の座標
    left, top = 0, 0
    #トリミングする右上の座標
    right, bottom = self.width, Findhood().calc_hood()
    print(bottom)
    #画像ファイル名を取得
    files = os.listdir(self.ORIGINAL_FILE_DIR)
    #特定の拡張子のファイルだけを採用。実際に加工するファイルの拡張子に合わせる
    files = [name for name in files if name.split(".")[-1] in ["png","jpg"]]

    for val in files:
      #オリジナル画像へのパス
      path = self.ORIGINAL_FILE_DIR + val
      #トリミングされたimageオブジェクトを取得
      im_trimmed = self.trim(path, left, top, right, bottom)
      #トリミング後のディレクトリに保存。ファイル名の頭に"cut_"をつけている
      im_trimmed.save(self.TRIMMED_FILE_DIR+val, quality=95) #qualityは95より大きい値は推奨されていないらしい
    return str("["+str(right)+","+str(bottom)+"]")
TrimImages().createTrimedImages()
  

