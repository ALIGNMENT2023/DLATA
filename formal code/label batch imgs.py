# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:00:16 2022

@author: luomoxuan
"""

from PIL import Image
from matplotlib.pylab import *
import numpy as np
from PIL import ImageFile

def choose_folder(): 
    
     # to provide a simple GUI to select the folder including the data images
   
    try:
        import tkinter
    except ImportError:
        print("Tkinter not installed.")
        exit()
        
    from tkinter import filedialog
    
    
    root = tkinter.Tk()
    
    root.withdraw()
    
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    
    return dirname

def get_name():
 
     # to provide a simple GUI to input the name of video   
 
    try:
        import tkinter
    except ImportError:
        print("Tkinter not installed.")
        exit()    
    root = tkinter.Tk()
    
    root.withdraw()
        
    name = tkinter.simpledialog.askstring('file name', 'Input String',parent=root, initialvalue='text.pkl')
    
    return name

def file_filter(f,Format='.jpg'):
    
     # to select a file with specific format
    
    if f[-4:] in [Format]:
        return True
    else:
        return False  


def sub_dir_path(dirpath):

     # to get the paths of all files under the folder
    
    import os
    
    dirs=os.listdir(dirpath)
    
    for i in range(len(dirs)):

        dirs[i]=dirpath+'/'+dirs[i]
   
           
    return dirs


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



import pickle

Dir=choose_folder()  # choose the folder
file_list=sub_dir_path(Dir)
x_y_list=[]
num_of_points=26 # set the number of the points

for i in range(len(file_list)):
    if file_filter(file_list[i]):
        x_y_list+=[dot_label(file_list[i],num_of_points)]  

name=get_name()

with open(Dir+'/'+name, 'wb') as f:
    pickle.dump(x_y_list, f)       # save the file
  
        