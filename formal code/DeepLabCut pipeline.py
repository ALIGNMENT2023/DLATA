# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:44:06 2022

@author: luomoxuan
"""

import deeplabcut

config_path = deeplabcut.create_new_project('Name of the project','Name of the experimenter',['Full path of video 1',],working_directory='Full path of the working directory',copy_videos=True)

# revise config.yaml in the relevant folder, to know more details, see the DeepLabCut paper

deeplabcut.extract_frames(config_path,'automatic','uniform')#'automatic/manual','uniform/kmeans'

deeplabcut.label_frames(config_path)

deeplabcut.check_labels(config_path)

deeplabcut.create_training_dataset(config_path,num_shuffles=1)

deeplabcut.train_network(config_path,shuffle=1,trainingsetindex=0,gputouse=None,max_snapshots_to_keep=5,
autotune=False,displayiters=None,saveiters=None)

deeplabcut.evaluate_network(config_path, Shuffles=[1], plotting=True, show_errors=True, comparisonbodyparts='all', gputouse=None)

deeplabcut.analyze_videos(config_path,['video_path'], shuffle=1, trainingsetindex=0, videotype='avi', gputouse=None, save_as_csv=True) # example: '/analysis/project/videos/reachingvideo1.avi'

deeplabcut.create_labeled_video(config_path, ['videos_names'], shuffle=1, trainingsetindex=0, videotype='avi', save_frames=False, delete=False, displayedbodyparts='all', codec='mp4v')

# the command line can be run one by one