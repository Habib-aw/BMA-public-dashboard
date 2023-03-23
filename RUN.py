# -*- coding: UTF-8 -*-
from tkinter import Tk,Label
from Slide import *
from Footer import *
from Slideshow import *
from hijri_converter import Gregorian
from datetime import datetime
from PIL import Image,ImageTk

root = Tk()
slideshow =Slideshow(root)
f =Footer(root)

s1 = Slide(root,
title="",
content="Baitul Ma'mur Academy",
contentFont=210,
paddingCtop=27.5
)
hijri = Gregorian(int(datetime.now().year), datetime.now().month, datetime.now().day).to_hijri()

if hijri.month_name() =="Ramadhan":
    try:
        openedImage = Image.open("images/Ramadan/"+str(hijri.day)+".jpg")
    except:
        openedImage = Image.open("images/Ramadan/noImgFound.png")
    width, height = openedImage.size
    maxImgWidth = 1900
    maxImgHeight=875
    imgWidth = round((width/height)*maxImgHeight)
    imgHeight = maxImgHeight
    if imgWidth>maxImgWidth:
        imgWidth=maxImgWidth
        imgHeight=round((height/width)*maxImgWidth)
    image = ImageTk.PhotoImage(openedImage.resize((imgWidth,imgHeight),Image.Resampling.LANCZOS))
    ramadanMessage = Slide(root,None,image=image,title="")


s1.packSlide()

slideshow.addAll([s1])
try:
    slideshow.add(ramadanMessage)
except:
    pass


slideshow.redoTimes()
root.config(bg=background)
root.attributes('-fullscreen',True)
root.mainloop()
