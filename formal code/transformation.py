# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 23:11:23 2022

@author: luomoxuan
"""
'''
import matlab
import matlab.engine
if __name__ == '__main__':
    eng = matlab.engine.start_matlab('MATLAB_R2018a')
    1
    eng.alignment_based_on_dots('小鼠脑图谱_页面_045 副本.png','77925097_248.jpg',nargout=0)
    #t = eng.myls(4,2)
    #print(t)
'''

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

def file_filter(f):

    # to select a file with specific format    
    
    if f[-4:] in ['.mat']:
        return True
    else:
        return False  

def read_map_points(csv_name='Hippo testDeepCut_resnet50_SliceHippoJun30shuffle1_50000.csv'):

    # get the coordinates of the predicted points

    x=pd.read_csv(csv_name,skiprows=[0,1]) # skip the first row
    y=x[x.columns.drop(list(x.filter(regex='coords')))] # delete the specific contents
    y=y[y.columns.drop(list(y.filter(regex='likelihood')))] # delete the specific contents

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
    


import matlab
import matlab.engine
from tkinter import filedialog
import numpy as np

if __name__ == '__main__':
    
    
    #map_file_data = io.loadmat('brain_atlas.mat')['mp'].tolist()  # Read the mat data for the feature points on atlas map 
    map_file_data = np.loadtxt('brain_atlas.csv').tolist()  # Read the mat data for the feature points on atlas map 
    eng = matlab.engine.start_matlab('MATLAB_R2018a')  # Input MATLAB Version
    
    map_data=matlab.double(map_file_data)
    
    
    dirpath=choose_folder()
    outcome_dir=choose_folder()
    imgs=sub_dir_path(dirpath)

    csv_path = 'Hippo testDeepCut_resnet50_SliceHippoJun30shuffle1_50000.csv' # path of the predicted points data
    
    map_img_path = 'test.png'  # image of the atlas map

    img_data_list=read_map_points(csv_name=csv_path)
    
    
    
    for i in range(len(imgs)):
    
        figure_data=matlab.double(img_data_list[i].tolist())
        eng.alignment_based_on_dots(map_img_path,imgs[i],map_data,figure_data,outcome_dir+'/'+'align-'+imgs[i].split('/')[-1],nargout=0) #
    
  