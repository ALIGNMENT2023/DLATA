# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:22:57 2022

@author: luomoxuan
"""

from PIL import  Image
import os


def choose_folder():
    try:
        import tkinter
    except ImportError:
        print("Tkinter not installed.")
        exit()
        
    from tkinter import filedialog
    
    #Suppress the Tkinter root window
    root = tkinter.Tk()
    
    root.withdraw()
    
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    
    return dirname

size=(500,400) # set the size 
path=choose_folder()  # select the folder including raw images
for maindir, subdir,file_name_list in os.walk(path):
    print(file_name_list)
    for file_name in file_name_list:
        image=os.path.join(maindir,file_name) # get the path of every image
        file=Image.open(image)
        out=file.resize(size,Image.ANTIALIAS)  # resize
        out.save(image)  
