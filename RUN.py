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

spaces = "    "
qrCode = ImageTk.PhotoImage(Image.open("images/BMA donate qr code.png").resize((890,890),Image.Resampling.LANCZOS))
s2 = Slide(root,
title="",
content=spaces+"Please Donate by\n"+spaces+"following the QR code\n\n\n"+spaces+"Or donate via\n"+spaces+"the donate page\n"+spaces+"on the website",
contentFont=60,
image=qrCode,
time=8
)
def fitImg(imgPath):
    openedImage = Image.open("images/"+imgPath)
    width, height = openedImage.size
    maxImgWidth = 1900
    maxImgHeight=875
    imgWidth = round((width/height)*maxImgHeight)
    imgHeight = maxImgHeight
    if imgWidth>maxImgWidth:
        imgWidth=maxImgWidth
        imgHeight=round((height/width)*maxImgWidth)
    return ImageTk.PhotoImage(openedImage.resize((imgWidth,imgHeight),Image.Resampling.LANCZOS))
maktab1 = fitImg("Maktab.jpg")
maktab2 = fitImg("Maktab1.JPG")

m1 = Slide(root,None,image=maktab1,title="",time=10)
m2 = Slide(root,None,image=maktab2,title="")

hijri = Gregorian(int(datetime.now().year), datetime.now().month, datetime.now().day).to_hijri()
if hijri.month_name() =="Dhu al-Hijjah":
    if hijri.day <10 and hijri.day>3:
        eidJamaahSlide = Slide(root,title="EID JAMA'AH",content="1st Jama'ah: 7:00 AM\n\n2nd Jama'ah: 8:30 AM\n\n3rd Jama'ah: 10:00 AM",contentFont=100,bg='black')
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
    if hijri.day >25:
        eidJamaahSlide = Slide(root,title="EID JAMA'AH",content="1st Jama'ah: 7:00 AM\n\n2nd Jama'ah: 8:30 AM\n\n3rd Jama'ah: 9:30 AM",contentFont=100,bg='black')
    if hijri.day <= 12 and hijri.year == 1444:
        gatheringSlide = Slide(root, title="Iftaar gathering this monday",titleFont=100,content="On monday 3rd of April (12th Ramadan),\nBaitul Mamur Academy would like to invite you to an iftaar gathering,\nPlease come and bring your friends & family to this barakah filled event\nWe look forward to seeing you all\nInsha'Allah",contentFont=65,time=10)
if (hijri.month_name()=="Shawwal" and hijri.day ==1) or (hijri.month_name()=="Dhu al-Hijjah" and hijri.day==10):
    eidMubarakSlide = Slide(root,title="",content="Eid Mubarak",contentFont=250,smallContent="TaqabbalAllahu Minna Wa Minkum",smallContentFont=50)


s1.packSlide()

slideshow.addAll([s1,s2,m1,m2])
try:
    slideshow.add(gatheringSlide)
except:
    pass
try:
    slideshow.add(ramadanMessage)
except:
    pass
try:
    slideshow.add(eidJamaahSlide)
except:
    pass
try:
    slideshow.add(eidMubarakSlide)
except:
    pass
slideshow.redoTimes()
root.config(bg=background)
root.attributes('-fullscreen',True)
root.mainloop()
