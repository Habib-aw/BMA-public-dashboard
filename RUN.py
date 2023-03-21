# -*- coding: UTF-8 -*-
from tkinter import Tk,Label
from Slide import *
from Footer import *
from Slideshow import *


root = Tk()
slideshow =Slideshow(root)
f =Footer(root)

s1 = Slide(root,
title="Slide 1",
content="Information goes here",
contentFont=60
)
s2 = Slide(root,
title="Slide 2",
content="Other information goes here",
contentFont=60
)
s1.packSlide()

slideshow.addAll([s1,s2])

slideshow.redoTimes()
root.config(bg=background)
root.attributes('-fullscreen',True)
root.mainloop()
