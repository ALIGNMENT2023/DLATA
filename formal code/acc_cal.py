# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 23:11:23 2022

@author: luomoxuan
"""

import pandas as pd
import numpy as np
import scipy.io as io 


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

def sub_dir_path(dirpath):

     # to get the paths of all files under the folder
    
    import os
    
    dirs=os.listdir(dirpath)
    
    for i in range(len(dirs)):

        dirs[i]=dirpath+'/'+dirs[i]
   
           
    return dirs

def file_filter(f,Type='.mat'):
    
    # to select a file with specific format
    
    if f[-4:] in [Type]:
        return True
    else:
        return False  

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

def read_map_points(csv_name='Hippo testDeepCut_resnet50_SliceHippoJun30shuffle1_50000.csv'):
    
    # get the coordinates of the predicted points
    
    x=pd.read_csv(csv_name,skiprows=[0,1]) # skip the first row
    y=x[x.columns.drop(list(x.filter(regex='coords')))] # delete the specific contents
    y=y[y.columns.drop(list(y.filter(regex='likelihood')))] # delete the specific contents
    #y=x[~x['A'].isin(["likelihood"])] 
    cord_x=y[y.columns.drop(list(y.filter(regex='y')))] # delete the specific contents
    cord_y=y[y.columns.drop(list(y.filter(regex='x')))] # delete the specific contents
    
    cord_x_value=pd.DataFrame(cord_x.values.T) #transpose
    cord_y_value=pd.DataFrame(cord_y.values.T)
    
    x_outcome=cord_x_value.to_numpy()
    y_outcome=cord_y_value.to_numpy()
    
    img_data_list=[]
    for i in range(len(x_outcome[0])):
        img_data_list+=[np.hstack((x_outcome[:,i:i+1],y_outcome[:,i:i+1]))]
    
    return img_data_list
    

import pickle
import numpy

if 1:
    Dir=choose_folder()
    file_list=sub_dir_path(Dir)
    for file in file_list:
        if file_filter(file,'.csv'):
            outcome=read_map_points(csv_name=file)
            
        if file_filter(file,'.pkl'):
            with open(file, 'rb') as f:
                label = pickle.load(f)  
                
    error=[]
    for i in range(len(label)):
        error+=[outcome[i]-label[i]]

    distance=[]
    for i in range(len(label)):
        distance+=[np.power(error[i][:,0]**2+error[i][:,1]**2,0.5)]
        
    final_outcome=distance[0].copy()
    for i in range(1,len(label)):
        final_outcome+=distance[i]
    final_outcome=final_outcome/len(label)
    txt_name=get_name()
    np.savetxt(txt_name,final_outcome) 
  


