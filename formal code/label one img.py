# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:23:51 2022

@author: luomoxuan
"""
from PIL import Image
from matplotlib.pylab import *
import numpy as np
from PIL import ImageFile
import numpy as np
import pickle

def dot_label(file_name='',num=3):
    
     # to label the feature points in the picture    
    
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    Image.MAX_IMAGE_PIXELS = None
    im = array(Image.open(file_name))
    imshow(im)
    print(file_name)
    print ('Please click '+str(num)+' points')
    x =ginput(num,timeout=999999999999999)
    y=np.array(x)
    #show()
    return y

def get_name():
 
     # to provide a simple GUI to input the name of video   
 
    try:
        import tkinter
    except ImportError:
        print("Tkinter not installed.")
        exit()    
    root = tkinter.Tk()
    
    root.withdraw()
        
    name = tkinter.simpledialog.askstring('file name', 'Input String',parent=root, initialvalue='text.csv')
    
    return name

def choose_file(): 
    
     # to provide a simple GUI to select the file
   
    try:
        import tkinter
    except ImportError:
        print("Tkinter not installed.")
        exit()
        
    from tkinter import filedialog
    
    
    root = tkinter.Tk()
    
    root.withdraw()
    
    filename = filedialog.askopenfilename(parent=root,initialdir="/",title='Please select a file')
    
    return filename

    
file_path=choose_file()  # choose the image

x_y_list=[]
num_of_points=26 # set the number of the points

dots_coor=dot_label(file_path,num_of_points)
name=get_name()
np.savetxt(name,dots_coor)  # save the file
  