# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:35:27 2022

@author: luomoxuan
"""

import os
import cv2

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
        
    name = tkinter.simpledialog.askstring('video name', 'Input String',parent=root, initialvalue='text.avi')
    
    return name

path = choose_folder()  # select the folder including images
filelist = os.listdir(path)  # select the images under the folder
filelist = sorted(filelist)  # sort the images

fps = 10  # set the video fps
size = (500, 400)  # set the video size
video_name=get_name() # set the video name  default: 'test.avi'

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size) # set the format of the video
# save the video in the current folder

for item in filelist:     # convert the images to the video
    if item.endswith('.jpg'):  # the format of the images
        # jpg, png, TIF...
        item = path + item
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()  # finish
