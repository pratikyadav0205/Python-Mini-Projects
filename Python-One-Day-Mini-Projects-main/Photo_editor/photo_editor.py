from importlib.resources import path
from PIL import Image, ImageEnhance, ImageFilter
import os

path = './img'
pathout = './edited'

for files in os.listdir(path):
    img = Image.open(f"{path}/{files}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    
name = os.path.splitext(files)[0]
edit.save(f"{pathout}/{name}_edited.jpg")
